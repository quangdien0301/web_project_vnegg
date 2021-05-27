from django.shortcuts import render
from courses.models import Course
# Create your views here.
def home_view(request):
    object_list = Course.objects.filter()
    return render(request,'home.html', {
        'object_list': object_list,
        'nav': 'home'
    })

def about_view(request):
    return render(request, 'about.html', { 'nav': 'about'})