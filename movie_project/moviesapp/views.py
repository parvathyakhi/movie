from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import movieform
from .models import movie
# Create your views here.
def index(request):
    obj=movie.objects.all()
    return render(request,'index.html',{'result':obj})
def detail(request,movie_id):
    movi=movie.objects.get(id=movie_id)
    return render(request,'details.html',{'movie1':movi})
def add_movie(request):
    if request.method == 'POST':
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        movies=movie(name=name,desc=desc,year=year,img=img)
        movies.save()
    return render(request,'add_movie.html')

def update(request,id):
    movie1=movie.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=movie1)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie1})

def delete(request,id):
    if request.method == 'POST':
        movie2=movie.objects.get(id=id)
        movie2.delete()
        return redirect('/')
    return render(request,'delete.html')