from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('movie/<int:movies_id>', views.get_movie_details, name='get_movie_details'),
    path('director/<int:director_id>', views.get_director_details, name='get_director_details'),
    path('actor/<int:actor_id>', views.get_actor_details, name='get_actor_details'),
    # path('analytics', views.analytics, name='analytics'),
]



