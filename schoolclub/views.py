import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
import random
from .models import User, School, Comment, Universities, Favourite
from .forms import UNiversities_form
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.views.decorators.http import require_http_methods

def index(request):
    schools = School.objects.all()
    if schools is None:
        return render(request, "school/index.html",{
        "active":False
    })
    return render(request, "school/index.html",{
        "active":schools
    })

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "school/register.html", {
                "message": "Passwords must match."
            })

    
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "school/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "school/register.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

  
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "school/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "school/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def api(request):
    UNiversitiess = Universities.objects.filter(user=request.user)
    UNiversitiess = UNiversitiess.order_by("-timestamp").all()
    return JsonResponse([UNiversities.serialize() for UNiversities in UNiversitiess], safe=False)

@login_required(login_url='/')
def profile(request):
    UNiversitiess = Universities.objects.all()
    return render(request, "school/profile.html", {
        'UNiversitiess':UNiversitiess})

@login_required(login_url='/')
def filterby(request):
    if request.method == "GET":
        return render(request, "school/filterby.html")
    else:
        location = request.POST["location"]
        accrate = request.POST["accrate"]
        if (location=="all" and accrate == "any"):
            schools= School.objects.all()
        elif (location == "all"):
            schools= School.objects.filter(accrate=accrate)
        elif (accrate == "any"):
            schools= School.objects.filter(location=location)
        else:
            schools= School.objects.filter(location=location, accrate=accrate)
        if len(schools)>0:
            boolean = True
        else:
            boolean = False
        return render(request, "school/filterby.html", {
            "active": schools, 
            "boolean": boolean
            })

@login_required(login_url="/")
def singlecollege(request, id):
    school = School.objects.get(id=id)
    userfavourite = Favourite.objects.filter(user=request.user).values('school_id')

    favourite = []
    for content in userfavourite:
        favourite.append(content['school_id'])
    if id in favourite:
        boolean = True
    else:
        boolean = False

    comments = Comment.objects.filter(school=school).values('id')
    comment_list = []
    for content in comments:
        comment = Comment.objects.get(id=content['id'])
        comment_list.append(comment)
    form = UNiversities_form()
    return render(request, "school/singlecollege.html", {
            "school": school,
            "comments":comment_list,
            "favourite":boolean,
            "form":form
            })

@login_required(login_url='/')
def favourite(request):
    user = request.user
    schools =Favourite.objects.filter(user=user).values('school_id')
    favourite= []
    for school in schools:
            favo = School.objects.get(id = school['school_id'])
            favourite.append(favo)
    if favourite is None:
        return render(request, "school/favourite.html", {
            "favourite":False
        })
    return render(request, "school/favourite.html",{
        "favourite": favourite
    })

@login_required(login_url='/')
def favswitcher(request,id):
    user = request.user
    school = School.objects.get(id=id)
    if Favourite.objects.filter(user=user, school=school).exists():
        favo = Favourite.objects.get(user=user,school=school)
        favo.delete()
        return HttpResponseRedirect(reverse("singlecollege", args=(),
            kwargs={'id': id}))
    else:
        favo = Favourite(user=user, school=school)
        favo.save()
        return HttpResponseRedirect(reverse("singlecollege", args=(),
            kwargs={'id': id}))

    
@login_required(login_url='/')
def UNiversities(request):
    if request.method == "POST":
        form = UNiversities_form(request.POST)
        if form.is_valid():
            UNiversities = form.save(commit=False)
            UNiversities.user = request.user
            UNiversities.book_number = random.randrange(10000, 99999)
            UNiversities.college = request.POST["college"]
            UNiversities.save()
        return HttpResponseRedirect(reverse("profile"))
    else:
        form = UNiversities_form()
        return render (request, "school/singlecollege.html",
         {'form':form
          })

@login_required(login_url='/')
def comment(request, id):

    user= request.user
    school= School.objects.get(id =id)
    if request.method == "POST":
        comment = request.POST.get("comment")
        new_comment= Comment (user = user, school =school, comment=comment)
        new_comment.save()

    return HttpResponseRedirect(reverse("singlecollege", args=(), kwargs={'id':id}))




