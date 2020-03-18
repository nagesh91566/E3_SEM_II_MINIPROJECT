from django.contrib import admin
from .models import *

movie_set = [Movie,Director,Cast,Actor]
admin.site.register(movie_set)