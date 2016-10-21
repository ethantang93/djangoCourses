from django.shortcuts import render, HttpResponse,redirect
from . import models
# Create your views here.
def index(request):
    course = models.Courses.objects.all()
    context ={ 'course':course}
    return render(request,'courses/index.html', context)
def addcourse(request):
    print request.method
    name = request.POST['name']
    print name
    description= request.POST['description']
    print description
    course = models.Courses.objects.create(name=name, description=description)
    return redirect('/')
def delete(request,id):
    deleteuser=models.Courses.objects.get(id=id).delete()
    return redirect('/')
