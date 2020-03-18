from django.shortcuts import render,get_object_or_404

from .models import *

def home(request):
    movie_list = Movie.objects.all()
    movies = []
    for movie in movie_list:
        movie.director = movie.director
        movies.append(movie)
    context = {'movie_list':movies}
    return render(request, 'imdb_home.html',context)

def get_movie_details(request,movies_id):
    movies = get_object_or_404(Movie,pk = movies_id)
    actors_of_movie = movies.actors.all()
    roles_of_movie = movies.cast_set.all()
    context = {"movies":movies,'actors_of_movie':actors_of_movie,'roles_of_movie':roles_of_movie}
    return render(request, 'imdb_movie.html',context)

def get_actor_details(request,actor_id):
    actor = get_object_or_404(Actor,pk = actor_id)
    movies_of_actor = actor.movie_set.all()
    context = {'actor':actor,'movies_of_actor':movies_of_actor}
    return render(request, 'imdb_actor.html',context)

def get_director_details(request,director_id):
    directors = get_object_or_404(Director,pk = director_id)
    movies_of_director = directors.movie_set.all()
    context = {'directors':directors,'movies_of_director':movies_of_director}
    return render(request, 'imdb_director.html',context)

# def get_movie_collections_polar_chart_data():
#     import json

#     from .models import Movie

#     movie_collections = Movie.objects.values_list('box_office_collection_in_crores',flat = True)
#     movie_ids = Movie.objects.values_list('movie_id',flat = True)


#     polar_chart_data = {
#         "datasets": [{
#             "data": list(movie_collections),
#             "backgroundColor": [
#                 "rgb(255, 0, 0)",
#                 "rgb(64, 255, 0)",
#                 "rgb(255, 0, 191)",
#                 "rgb(64, 0, 255)",
#                 "rgb(0, 255, 191)"
#             ]

#         }],
#         "labels": list(movie_ids),
#     }
#     return {
#         'polar_chart_data_one': json.dumps(
#             polar_chart_data),
#         'polar_chart_data_one_title': 'Title'
#     }


# def get_top_movies_collections_one_bar_plot_data():
#     import json

#     from .models import Movie

#     movie_collections = Movie.objects.values_list('box_office_collection_in_crores',flat = True)
#     movie_names = Movie.objects.values_list('name',flat = True)
#     single_bar_chart_data = {
#         "labels": list(movie_names),
#         "datasets":[
#             {
#                 "data": list(movie_collections),
#                 "label": "Collections",
#                 "borderColor": "rgba(0, 123, 255, 0.9)",
#                 "border_width": "0",
#                 "backgroundColor": [
#                 "rgb(255, 0, 0)",
#                 "rgb(64, 255, 0)",
#                 "rgb(255, 0, 191)",
#                 "rgb(64, 0, 255)",
#                 "rgb(0, 255, 191)"
#             ]
#             }
#         ]
#     }
#     return {
#         'single_bar_chart_data_one': json.dumps(single_bar_chart_data),
#         'single_bar_chart_data_one_title': 'Top Movies Collections '
#     }


# def get_movie_collections_doughnut_chart_data():
#     import json
#     from .models import Movie

#     movie_collections = Movie.objects.values_list('box_office_collection_in_crores',flat = True)
#     movie_ids = Movie.objects.values_list('movie_id',flat = True)

#     doughnut_graph_data = {
#         "datasets": [{
#             "data":  list(movie_collections),
#             "backgroundColor": [
#                 "rgb(255, 0, 0)",
#                 "rgb(64, 255, 0)",
#                 "rgb(255, 0, 191)",
#                 "rgb(64, 0, 255)",
#                 "rgb(0, 255, 191)"
#             ],
#             "hoverBackgroundColor": [
#                 "rgba(0, 123, 255,0.9)",
#                 "rgba(0, 123, 255,0.7)",
#                 "rgba(0, 123, 255,0.5)",
#                 "rgba(0,0,0,0.07)"
#             ]

#         }],
#         "labels": list(movie_ids),
#     }

#     return {
#         'doughnut_graph_data_one': json.dumps(doughnut_graph_data),
#         'doughnut_graph_data_one_title': 'Title'
#     }

# def get_multi_line_plot_with_area_data():
#     import json

#     years = execute_sql_query( '''
#                    select strftime('%Y',release_year) from imdb_movie group by strftime('%Y',release_year) limit 5;
#             ''')

#     remunration = execute_sql_query( '''
#                    select sum(remunration_in_crores) 
#                         from (imdb_movie as movie
#                             inner join imdb_cast as cast)
#                         inner join imdb_actor as actor
#                         on `movie`.movie_id = `cast`.movie_id and `actor`.actor_id=`cast`.actor_id
#                         and `actor`.actor_id = 15661001
#                         group by strftime('%Y',release_date)
#                         ;''')

#     print(remunration)
#     multi_line_plot_with_area_data = {
#         "labels": list(years),
#         "defaultFontFamily": "Poppins",
#         "datasets": [
#             {
#                 "label": "Prabhas Remuneration",
#                 "borderColor": "rgba(0,0,0,.09)",
#                 "borderWidth": "1",
#                 "backgroundColor": "rgb(255, 0, 255)",
#                 "data":list(remunration),
#             }
#         ]
#     }

#     return {
#         'multi_line_plot_with_area_data_one': json.dumps(
#             multi_line_plot_with_area_data),
#         'multi_line_plot_with_area_data_one_title': 'Prabhas Remuneration in Year_wise'
#     }

# def get_yearwise_budget_vs_collections_two_bar_plot_data():
#     import json

#     movie_budget = execute_sql_query( '''
#                     select avg(budget_in_crores) from imdb_movie group by strftime('%Y',release_date) limit 5;
#             ''')

#     movie_collections = execute_sql_query( '''
#                     select avg(box_office_collection_in_crores) from imdb_movie group by strftime('%Y',release_date) limit 5;
#             ''')
    
#     years = execute_sql_query( '''
#                    select strftime('%Y',release_date) from imdb_movie group by strftime('%Y',release_date) limit 5;
#             ''')

#     print(years)
#     multi_bar_plot_data = {
#         "labels": list(years),
#         "datasets": [
#             {
#                 "label": "Movie Budget",
#                 "data": list(movie_budget),
#                 "borderColor": "rgba(0, 123, 255, 0.9)",
#                 "borderWidth": "0",
#                 "backgroundColor": "rgb(255, 0, 0)",
#                 "fontFamily": "Poppins"
#             },
#             {
#                 "label": "Movie Collections",
#                 "data": list(movie_collections),
#                 "borderColor": "rgba(0,0,0,0.09)",
#                 "borderWidth": "0",
#                 "backgroundColor": "rgb(64, 255, 0)",
#                 "fontFamily": "Poppins"
#             }
#         ]
#     }

#     return {
#         'multi_bar_plot_data_one': json.dumps(multi_bar_plot_data),
#         'multi_bar_plot_data_one_title': 'Year_wise Movie Budget vs Collections'
#     }

# def get_movie_genres_percentage_pie_chart_data():
#     import json

#     movies_genre_percent = execute_sql_query( '''
#                     select count(genre)*100/
#                         (select count(genre) 
#                         from imdb_movie)
#                     from imdb_movie 
#                     group by genre;
#             ''')

#     movie_genre = execute_sql_query( '''
#                     select distinct(genre) from imdb_movie;
#             ''')
#     print(movies_genre_percent)
#     pie_chart_data = {
#         "datasets": [{
#             "data": list(movies_genre_percent),
#             "backgroundColor": [
#                 "rgb(255, 0, 0)",
#                 "rgb(64, 255, 0)",
#                 "rgb(255, 0, 191)",
#                 "rgb(64, 0, 255)",
#                 "rgb(0, 255, 191)"
#             ],
#             "hoverBackgroundColor": [
#                 "rgba(0, 123, 255,0.9)",
#                 "rgba(0, 123, 255,0.7)",
#                 "rgba(0, 123, 255,0.5)",
#                 "rgba(0,0,0,0.07)"
#             ]

#         }],
#         "labels": list(movie_genre)
#     }

#     return {
#         'pie_chart_data_one': json.dumps(
#             pie_chart_data),
#         'pie_chart_data_one_title': 'Movies Genre in Percentage'
#     }

# def get_movie_average_rating_yearwise_multi_line_plot_data():
#     import json

#     movie_collections = execute_sql_query( '''
#                     select avg(box_office_collection_in_crores) from imdb_movie group by strftime('%Y',release_date);
#             ''')

#     movie_avg_rating = execute_sql_query( '''
#                     select avg_rating/count(avg_rating)
                        
#                     from imdb_movie 
#                     group by strftime('%Y',release_date);
#             ''')
    
#     years = execute_sql_query( '''
#                    select strftime('%Y',release_date) from imdb_movie group by strftime('%Y',release_date);
#             ''')

    

#     multi_line_plot_data = {
#         "labels": list(years),
#         "type": 'line',
#         "defaultFontFamily": 'Poppins',
#         "datasets": [{
#             "label": "Average_Rating",
#             "data": list(movie_avg_rating),
#             "backgroundColor": 'transparent',
#             "borderColor": 'rgba(40,167,69,0.75)',
#             "borderWidth": 3,
#             "pointStyle": 'circle',
#             "pointRadius": 5,
#             "pointBorderColor": 'transparent',
#             "pointBackgroundColor": 'rgba(40,167,69,0.75)',
#         }]
#     }
#     return {
#         'multi_line_plot_data_one': json.dumps(multi_line_plot_data),
#         'multi_line_plot_data_one_title': 'Year_wise Movies Average_Rating'
#     }
# def analytics(request):

#     import json
#     bar_data = get_top_movies_collections_one_bar_plot_data()
#     # polar_data = get_movie_collections_polar_chart_data()
#     # doughnut_data = get_movie_collections_doughnut_chart_data()
#     multi_line_plot = get_multi_line_plot_with_area_data()
#     multi_bar = get_yearwise_budget_vs_collections_two_bar_plot_data()
#     pie_chart = get_movie_genres_percentage_pie_chart_data()
#     avg_rating = get_movie_average_rating_yearwise_multi_line_plot_data()
#     context = {}
#     context.update(bar_data)
#     # context.update(polar_data)
#     # context.update(doughnut_data)
#     context.update(multi_line_plot)
#     context.update(multi_bar)
#     context.update(pie_chart)
#     context.update(avg_rating)
#     # print('bar_data: ', bar_data)
#     # print(context)
#     return render(request, 'analytics.html',context = context)



# def execute_sql_query(sql_query):
#     """
#     Executes sql query and return data in the form of lists (
#         This function is similar to what you have learnt earlier. Here we are
#         using `cursor` from django instead of sqlite3 library
#     )
#     :param sql_query: a sql as string
#     :return:
#     """
#     from django.db import connection
#     with connection.cursor() as cursor:
#         cursor.execute(sql_query)
#         rows = cursor.fetchall()
#     return rows


