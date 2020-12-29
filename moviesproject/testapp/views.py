from django.shortcuts import render
from testapp.models import movie
from testapp.forms import movieform
# Create your views here.

def index_view(request):
    return render(request,'testapp/index.html')

def add_movie_view(request):
    form=movieform()
    if request.method=='POST':
        form=movieform(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return index_view(request)    
    return render(request,'testapp/form.html',{'form':form})

def movie_list_view(request):
    movies_list=movie.objects.all()
    return render(request,'testapp/display.html',{'movies_list':movies_list})
