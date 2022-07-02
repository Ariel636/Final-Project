from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class School(models.Model):
    locations = [
        ('New York, NY', 'New York, NY'),
        ('Cambridge, MA', 'Cambridge, MA'),
        ('Princeton, NJ', 'Princeton, NJ'),
        ('New Haven, CT', 'New Haven, CT'),
        ('Providence, RI', 'Providence, RI'),
        ('Philadelphia, PA', 'Philadelphia, PA'),
        ('Hanover, NH', 'Hanover, NH'),
        ('Ithaca, NY', 'Ithaca, NY')
    ]

    accrates = [
        ('3.0-3.9%', '3.0-3.9%'), 
        ('4.0-4.9%', '4.0-4.9%'), 
        ('5.0-5.9%', '5.0-5.9%'), 
        ('6.0-6.9%', '6.0-6.9%'), 
        ('7.0-7.9%', '7.0-7.9%'), 
        ('8.0-8.9%', '8.0-8.9%'), 
        ('9.0-9.9%', '9.0-9.9%')
    ]

    
    title = models.CharField(max_length= 70)
    location = models.CharField(choices=locations, max_length= 64, blank=True, default='Select location')
    accrate = models.CharField(choices=accrates, max_length= 64, blank=True, default='Select accrate')
    short_description = models.CharField(max_length=170, blank=True)
    description = models.CharField(max_length = 2000)
    image_url = models.URLField(blank=True)
    map_url = models.URLField(blank=True, max_length = 2000)
    status    = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"

class Favourite (models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE, related_name="use_favourite")
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="favourite_item")

    def __str__(self):
        return f"{self.user} {self.school}"

class Comment (models.Model):
    user      = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_colleger")
    school   = models.ForeignKey(School, on_delete=models.CASCADE, related_name="comment_school") 
    comment    = models.CharField(max_length=1800)

    def __str__(self):
        return f"{self.user} on {self.school} say {self.comment}"

class Universities(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    college = models.CharField(max_length= 120, blank=True)
    name = models.CharField(max_length= 70)
    last_name = models.CharField(max_length= 70)
    date = models.DateField()
    phone = models.CharField(max_length=64)
    book_number = models.CharField(max_length=64)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def serialize(self):
        return {
            "id": self.id,
            "college": self.college,
            "name": self.name,
            "last_name": self.last_name,
            "date": self.date,
            "phone": self.phone,
            "book_number": self.book_number,
            "timestamp": self.timestamp.strftime("%b %-d %Y, %-I:%M %p")
        }

