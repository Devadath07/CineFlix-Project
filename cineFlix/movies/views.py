from django.shortcuts import render,redirect

from django.views import View

from .models import Movie,IndustryChoices,GenreChoice,LanguageChoices,ArtistsChoices,CertificationChoice

from .forms import MovieForm

from django.db.models import Q


# Create your views here.
class HomeView(View):

    template = 'home.html'

    def get(self,request,*args, **kwargs):

        data = {'page':'Home'}

        return render(request,self.template,context=data)
    
class MoviesListView (View) :
     
     template = 'movies/movie-list.html'

     def get (self,request,*args,**kwargs) :

        query = request.GET.get('query')

        movies = Movie.objects.filter(activate_status=True)

        if query : 

            movies = movies.filter(Q(name__icontains=query)|
                                   Q(description__icontains=query)|
                                   Q(industry__name__icontains=query)|
                                   Q(certification__icontains=query)|
                                   Q(genre__name__icontains=query)|
                                   Q(artists__name__icontains=query)|
                                   Q(languages__name__icontains=query)|
                                   Q(tags__icontains=query)                        
                                   ).distinct()

        data = {'page':'Movies','movies':movies,'query':query}

        return render(request,self.template ,context=data)
     

# class MovieCreateView(View):

#     def get (self,request,*args, **kwargs):

#         industry_choices = IndustryChoices

#         genre_choices = GenreChoice

#         language_choices = LanguageChoices

#         artists_choices = ArtistsChoices

#         certification_choices = CertificationChoice


#         data = {'page':'create-movie','industry_choices': IndustryChoices,
#                 'genre_choices' : GenreChoice , 'language_choices' : LanguageChoices,
#                 'artists_choices' : ArtistsChoices , 'certification_choices' : CertificationChoice
#                 }

#         return render(request,'movies/movie-create.html',context=data)
    
#     def post(self,request,*args, **kwargs):

#         movie_data = request.POST

#         name = movie_data.get('name')

#         photo = request.FILES.get('photo')

#         description = movie_data.get('description')

#         release_date = movie_data.get('release_date')

#         runtime = movie_data.get('runtime')

#         certification = movie_data.get('certification')

#         industry = movie_data.get('industry')

#         languages = movie_data.get('languages')

#         genre = movie_data.get('genre')

#         artists = movie_data.get('artists')

#         video = movie_data.get('video')

#         tags = movie_data.get('tags')

#         Movie.objects.create(name=name,photo=photo,
#                              description=description,release_date=release_date,
#                              industry=industry,runtime=runtime,
#                              certification=certification,genre=genre,
#                              artists=artists,video=video,
#                              tags=tags,languages=languages)
#         return redirect('movie-list')
    
#Django Forms

class MovieCreateView(View):

    form_class = MovieForm # set as attribute

    template = 'movies/movie-create.html'

    def get (self,request,*args, **kwargs):

        form = self.form_class()

        data = {'page':'create-movie',
                'form': form
                }

        return render(request,self.template,context=data)
    
    #without form
    
    # def post(self,request,*args, **kwargs):

    #     movie_data = request.POST

    #     name = movie_data.get('name')

    #     photo = request.FILES.get('photo')

    #     description = movie_data.get('description')

    #     release_date = movie_data.get('release_date')

    #     runtime = movie_data.get('runtime')

    #     certification = movie_data.get('certification')

    #     industry = movie_data.get('industry')

    #     languages = movie_data.get('languages')

    #     genre = movie_data.get('genre')

    #     artists = movie_data.get('artists')

    #     video = movie_data.get('video')

    #     tags = movie_data.get('tags')

    #     Movie.objects.create(name=name,photo=photo,
    #                          description=description,release_date=release_date,
    #                          industry=industry,runtime=runtime,
    #                          certification=certification,genre=genre,
    #                          artists=artists,video=video,
    #                          tags=tags,languages=languages)
    #     return redirect('movie-list')
    
    #with form

    def post(self,request,*args, **kwargs):

        form = self.form_class(request.POST,request.FILES)

        #validation checks (from model)
        if form.is_valid():

            form.save()

            return redirect('movie-list')
        
        data = {'form':form,'page':'create-movie',}
    
        return render(request,self.template,context=data)

# implementing with ID
class MovieDetailsView(View):

    template = 'movies/movie-details.html'

    def get(self,request,*args, **kwargs):

        uuid = kwargs.get('uuid') # to access value

        movie = Movie.objects.get(uuid=uuid)

        data = {'movie':movie,'page':movie.name}

        return render(request,self.template,context=data)

# # using uuid

# class MovieDetailsView(View):

#     template = 'movies/movie-details.html'

#     def get(self,request,*args, **kwargs):

#         uuid = kwargs.get('uuid') # to access value

#         movie = Movie.objects.get(uuid=uuid)

#         data = {'movie':movie,'page':movie.name}

#         return render(request,self.template,context=data)

class MovieEditView(View):

    form_class = MovieForm

    template = 'movies/movie-edit.html'

    def get(self,request,*args, **kwargs):

        uuid = kwargs.get('uuid')

        movie = Movie.objects.get(uuid=uuid)

        form = self.form_class(instance=movie) # to edit a file with existing data pass as instance

        data = {'form':form,'page':movie.name}

        return render(request,self.template,context=data)
    
    def post(self,request,*args, **kwargs):

        uuid = kwargs.get('uuid')

        movie = Movie.objects.get(uuid=uuid)

        form = self.form_class(request.POST,request.FILES,instance=movie)
        if form.is_valid():

            form.save()

            return redirect('movie-details',uuid=uuid)
        
        data = {'form':form,'page':movie.name}

        return render(request,self.template,context=data)
    

class MovieDeleteView(View):

    def get(self,request,*args, **kwargs):

        uuid = kwargs.get('uuid')

        movie = Movie.objects.get(uuid=uuid)

        #hard delete - delete from database

        # movie.delete()

        movie.activate_status = False

        #softdelete

        movie.save()

        return redirect('movie-list')