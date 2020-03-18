from django.db import models

class Director(models.Model):
    director_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 10)
    # age = models.IntegerField()
    # base_remuneration_in_crores = models.FloatField()

    def __str__(self):
        return self.name

class Actor(models.Model):
    actor_id = models.CharField(max_length = 100,primary_key = True)
    name = models.CharField(max_length = 100)
    # date_of_birth = models.DateField()
    gender = models.CharField(max_length = 10)
    # age = models.IntegerField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length = 100)
    movie_id = models.CharField(max_length = 100,primary_key = True)
    release_year = models.IntegerField()
    avg_rating = models.FloatField()
    # movie_description = models.TextField()
    genre = models.CharField(max_length = 100)
    box_office_collection_in_crores = models.FloatField()
    budget_in_crores = models.FloatField()
    director = models.ForeignKey(Director,on_delete = models.CASCADE)
    actors = models.ManyToManyField(Actor,through = 'Cast',through_fields = ('movie','actor'))

    def __str__(self):
        return self.name

class Cast(models.Model):
    actor = models.ForeignKey(Actor,on_delete = models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete = models.CASCADE)
    role = models.CharField(max_length = 50)
    remunration_in_crores = models.FloatField()
    # is_debut_movie = models.BooleanField(default = False)

# class Rating(models.Model):
#     movie = models.OneToOneField(Movie,on_delete = models.CASCADE)
#     rating_one_count = models.IntegerField(default = 0)
#     rating_two_count = models.IntegerField(default = 0)
#     rating_three_count = models.IntegerField(default = 0)
#     rating_four_count = models.IntegerField(default = 0)
#     rating_five_count = models.IntegerField(default = 0)
