from django.urls import path

from . import views

urlpatterns = [

    path('',views.HomeView.as_view(),name='home'),

    path('movie-list',views.MoviesListView.as_view(),name='movie-list'),
    
]
