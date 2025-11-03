from django.shortcuts import render

from django.views import View

from .models import Movie

# Create your views here.
class HomeView(View):

    def get(self,request,*args, **kwargs):

        data = {'page':'Home'}

        return render(request,'home.html',context=data)
    
class MoviesListView (View) :

     def get (self,request,*args,**kwargs) :

        movies = Movie.objects.all()

        data = {'page':'Movies','movies':movies}

        return render(request,'movies/movie-list.html',context=data)