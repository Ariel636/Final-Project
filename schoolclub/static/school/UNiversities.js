document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#book').addEventListener('click', load_UNiversities);
    load_college('UNiversities-view');
});

function load_college() {
    document.querySelector('#UNiversities-view').style.display = 'none';
    document.querySelector('#map-view').style.display = 'block';
    document.querySelector('#comments-view').style.display ='block';
}

function load_UNiversities(){
    document.querySelector('#UNiversities-view').style.display = 'block';
    document.querySelector('#map-view').style.display = 'none';
    document.querySelector('#comments-view').style.display ='none';
}

function load_books() {
    document.querySelector('#UNiversities-view').style.display = 'none';
    document.querySelector('#map-view').style.display = 'none';
    document.querySelector('#comments-view').style.display ='none';
 }