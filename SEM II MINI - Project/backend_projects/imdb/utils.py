from .models import *

def get_one_bar_plot_data():
    import json
    single_bar_chart_data = {
        "labels": ["Sun", "Mon", "Tu", "Wed", "Th", "Fri", "Sat"],
        "datasets":[
            {
                "data": [40, 55, 75, 81, 56, 55, 40],
                "name": "Single Bar Chart",
                "borderColor": "rgba(0, 123, 255, 0.9)",
                "border_width": "0",
                "backgroundColor": "rgba(0, 123, 255, 0.5)"
            }
        ]
    }
    return {
        'single_bar_chart_data_one': json.dumps(single_bar_chart_data),
        'single_bar_chart_data_one_title': 'Title'
    }


def get_two_bar_plot_data():
    import json
    multi_bar_plot_data = {
        "labels": ["January", "February", "March", "April", "May", "June",
                   "July"],
        "datasets": [
            {
                "label": "My First dataset",
                "data": [65, 59, 80, 81, 56, 55, 40],
                "borderColor": "rgba(0, 123, 255, 0.9)",
                "borderWidth": "0",
                "backgroundColor": "rgba(0, 123, 255, 0.5)",
                "fontFamily": "Poppins"
            },
            {
                "label": "My Second dataset",
                "data": [28, 48, 40, 19, 86, 27, 90],
                "borderColor": "rgba(0,0,0,0.09)",
                "borderWidth": "0",
                "backgroundColor": "rgba(0,0,0,0.07)",
                "fontFamily": "Poppins"
            }
        ]
    }

    return {
        'multi_bar_plot_data_one': json.dumps(multi_bar_plot_data),
        'multi_bar_plot_data_one_title': 'Title'
    }


def get_multi_line_plot_data():
    import json
    multi_line_plot_data = {
        "labels": ["2010", "2011", "2012", "2013", "2014", "2015", "2016"],
        "type": 'line',
        "defaultFontFamily": 'Poppins',
        "datasets": [{
            "label": "Foods",
            "data": [0, 30, 10, 120, 50, 63, 10],
            "backgroundColor": 'transparent',
            "borderColor": 'rgba(220,53,69,0.75)',
            "borderWidth": 3,
            "pointStyle": 'circle',
            "pointRadius": 5,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgba(220,53,69,0.75)',
        }, {
            "label": "Electronics",
            "data": [0, 50, 40, 80, 40, 79, 120],
            "backgroundColor": 'transparent',
            "borderColor": 'rgba(40,167,69,0.75)',
            "borderWidth": 3,
            "pointStyle": 'circle',
            "pointRadius": 5,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgba(40,167,69,0.75)',
        }]
    }
    return {
        'multi_line_plot_data_one': json.dumps(multi_line_plot_data),
        'multi_line_plot_data_one_title': 'Title'
    }


def get_area_plot_data():
    import json
    area_plot_data = {
        "labels": ["2010", "2011", "2012", "2013", "2014", "2015", "2016"],
        "type": 'line',
        "defaultFontFamily": 'Poppins',
        "datasets": [{
            "data": [0, 7, 3, 5, 2, 10, 7],
            "label": "Expense",
            "backgroundColor": 'rgba(0,103,255,.15)',
            "borderColor": 'rgba(0,103,255,0.5)',
            "borderWidth": 3.5,
            "pointStyle": 'circle',
            "pointRadius": 5,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgba(0,103,255,0.5)',
        }, ]
    }
    return {
        'area_plot_data_one': json.dumps(area_plot_data),
        'area_plot_data_one_title': 'Title'
    }


def get_radar_chart_data():
    import json
    radar_chart_data = {
        "labels": [["Eating", "Dinner"], ["Drinking", "Water"], "Sleeping",
                   ["Designing", "Graphics"], "Coding", "Cycling", "Running"],
        "defaultFontFamily": 'Poppins',
        "datasets": [
            {
                "label": "My First dataset",
                "data": [65, 59, 66, 45, 56, 55, 40],
                "borderColor": "rgba(0, 123, 255, 0.6)",
                "borderWidth": "1",
                "backgroundColor": "rgba(0, 123, 255, 0.4)"
            },
            {
                "label": "My Second dataset",
                "data": [28, 12, 40, 19, 63, 27, 87],
                "borderColor": "rgba(0, 123, 255, 0.7",
                "borderWidth": "1",
                "backgroundColor": "rgba(0, 123, 255, 0.5)"
            }
        ]
    }
    return {
        'radar_chart_data_one': json.dumps(radar_chart_data),
        'radar_chart_data_one_title': 'Title'
    }


def get_doughnut_chart_data():
    import json
    doughnut_graph_data = {
        "datasets": [{
            "data": [45, 25, 20, 10],
            "backgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ],
            "hoverBackgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ]

        }],
        "labels": [
            "Green1",
            "Green2",
            "Green3",
            "Green4"
        ]
    }

    return {
        'doughnut_graph_data_one': json.dumps(doughnut_graph_data),
        'doughnut_graph_data_one_title': 'Title'
    }


def get_multi_line_plot_with_area_data():
    import json
    multi_line_plot_with_area_data = {
        "labels": [
            "January", "February", "March", "April", "May", "June",
            "July"],
        "defaultFontFamily": "Poppins",
        "datasets": [
            {
                "label": "My First dataset",
                "borderColor": "rgba(0,0,0,.09)",
                "borderWidth": "1",
                "backgroundColor": "rgba(0,0,0,.07)",
                "data": [22, 44, 67, 43, 76, 45, 12]
            },
            {
                "label": "My Second dataset",
                "borderColor": "rgba(0, 123, 255, 0.9)",
                "borderWidth": "1",
                "backgroundColor": "rgba(0, 123, 255, 0.5)",
                "pointHighlightStroke": "rgba(26,179,148,1)",
                "data": [16, 32, 18, 26, 42, 33, 44]
            }
        ]
    }

    return {
        'multi_line_plot_with_area_data_one': json.dumps(
            multi_line_plot_with_area_data),
        'multi_line_plot_with_area_data_one_title': 'Title'
    }


def get_pie_chart_data():
    import json

    pie_chart_data = {
        "datasets": [{
            "data": [45, 25, 20, 10],
            "backgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ],
            "hoverBackgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ]

        }],
        "labels": [
            "Green",
            "Green",
            "Green"
        ]
    }

    return {
        'pie_chart_data_one': json.dumps(
            pie_chart_data),
        'pie_chart_data_one_title': 'Title'
    }


def get_polar_chart_data():
    import json

    polar_chart_data = {
        "datasets": [{
            "data": [15, 18, 9, 6, 19],
            "backgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.8)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0,0,0,0.2)",
                "rgba(0, 123, 255,0.5)"
            ]

        }],
        "labels": [
            "Green1",
            "Green2",
            "Green3",
            "Green4",
            "Green5"
        ]
    }
    return {
        'polar_chart_data_one': json.dumps(
            polar_chart_data),
        'polar_chart_data_one_title': 'Title'
    }


def execute_sql_query(sql_query):
    """
    Executes sql query and return data in the form of lists (
        This function is similar to what you have learnt earlier. Here we are
        using `cursor` from django instead of sqlite3 library
    )
    :param sql_query: a sql as string
    :return:
    """
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute(sql_query)
        rows = cursor.fetchall()
    return rows


def populate_actors():
    import json

    actors_objs_list = open("/home/rgukt/Desktop/SEM II MINI - Project/complete_data/actors_5000.json",'r')
    actors_objs_read = actors_objs_list.read()
    actors_dict = json.loads(actors_objs_read)

    for actors in actors_dict:
        Actor.objects.create(actor_id = actors['actor_id'],
                            name = actors['name'],
                            gender = actors['gender'])




def populate_directors():
    import json

    directors_objs_list = open("/home/rgukt/Desktop/SEM II MINI - Project/complete_data/directors_5000.json",'r')
    directors_objs_read = directors_objs_list.read()
    directors_dict = json.loads(directors_objs_read)

    for directors in directors_dict:
        Director.objects.create(    
                                name = directors['name'],
                                gender = directors['gender'])

    

def populate_movies():
    import json

    movies_objs_list = open("/home/rgukt/Desktop/SEM II MINI - Project/complete_data/directors_5000.json",'r')
    movies_objs_read = movies_objs_list.read()
    movies_dict = json.loads(movies_objs_read)


    for movies in movies_dict:
        Movie.objects.create(movie_id = movies['movie_id'],
                             name = movies['name'],
                             avg_rating = movies['average_rating'],
                             release_year = movies['year_of_release'],
                             genre = movies['genres'][0],
                             budget_in_crores = movies['budget'],
                             box_office_collection_in_crores = movies['box_office_collection_in_crores'],
                             director = Director.objects.get(name = movies['director_name']))
        for actor_movies in movies['actors']:
            Cast.objects.create(actor = Actor.objects.get(actor_id = actor_movies['actor_id']),
                                movie = Movie.objects.get(movie_id = movies['movie_id']))




# def populate_database(actors_list, movies_list, directors_list):
#     import json

#     for actors in actors_list:
#         Actor.objects.create(actor_id = actors['actor_id'],name = actors['name'],date_of_birth = actors['date_of_birth'],age = actors['age'],gender = actors['gender'])

#     for directors in directors_list:
#         Director.objects.create(director_id = directors['director_id'], name = directors['name'],age = directors['age'],base_remuneration_in_crores = directors['base_remuneration_in_crores'])

#     for movies in movies_list:
#         Movie.objects.create(movie_id = movies['movie_id'],
#                              name = movies['name'],
#                              avg_rating = movies['avg_rating'],
#                              movie_description = movies['movie_description'],
#                              genre = movies['genre'],
#                              release_date = movies['release_date'],
#                              budget_in_crores = movies['budget_in_crores'],
#                              box_office_collection_in_crores = movies['box_office_collection_in_crores'],
#                              director = Director.objects.get(name = movies['director_name']))
#         for actor_movies in movies['actors']:
#             Cast.objects.create(actor = Actor.objects.get(actor_id = actor_movies['actor_id']),
#                                 movie = Movie.objects.get(movie_id = movies['movie_id']),
#                                 role = actor_movies['role'],
#                                 remunration_in_crores = actor_movies['remunration_in_crores'])



actors_list = [
        {
            "actor_id": "15661001",
            "name": "Prabhas",
            "date_of_birth": "1979-10-23",
            "age" : "40",
            "gender" : "Male"
        },
        {
            "actor_id": "15661002",
            "name": "Anushka",
            "date_of_birth": "1981-9-7",
            "age" : "38",
            "gender" : "Female"
        },
        {
            "actor_id": "15661004",
            "name": "Mahesh Babu",
            "date_of_birth": "1975-8-9",
            "age" : "44",
            "gender" : "Male"
        },
        {
            "actor_id": "15661005",
            "name": "Ram Charan",
            "date_of_birth": "1985-3-27",
            "age" : "34",
            "gender" : "Male"
        },
        {
            "actor_id": "15661006",
            "name": "Pawan Kalyan",
            "date_of_birth": "1971-9-2",
            "age" : "48",
            "gender" : "Male"
        }
    ]


movies_list = [
        {
            "movie_id": "15662001",
            "name": "Baahubali",
            "actors": [
                {
                    "actor_id": "15661001",
                    "role":"Mahendra Baahunali",
                    "remunration_in_crores":"50"
                },
                {
                    "actor_id": "15661002",
                    "role":"Devasena",
                    "remunration_in_crores":"20"
                }
            ],
            "box_office_collection_in_crores": "1200.3",
            "release_date": "2015-7-10",
            "director_name": "S. S. Rajamouli",
            "avg_rating":"9.2",
            "budget_in_crores":"900",
            "genre":"Action",
            "movie_description":"Baahubali: The Beginning is a 2015 South Indian epic action film directed by S. S. Rajamouli. ... In the process, he learns of his true identity as the heir to the throne of Mahishmati, the son of Amarendra Baahubali, whose tale is narrated to him by Kattappa, a loyal warrior."
        },

        {
            "movie_id": "15662002",
            "name": "Sarileru Neekevvaru",
            "actors": [
                {
                    "actor_id": "15661004",
                    "role":"Army Man",
                    "remunration_in_crores":"45"
                }
            ],
            "box_office_collection_in_crores": "700.4",
            "release_date": "2020-1-11",
            "director_name": "Anil Ravipudi",
            "avg_rating":"9.5",
            "genre":"Action and Adventure",
            "budget_in_crores":"400",
            "movie_description":"Sarileru Neekevvaru ( transl. 'Nobody can match you') is a 2020 Indian Telugu-language action comedy film written and directed by Anil Ravipudi. The film stars Mahesh Babu as Indian Army Major Ajay Krishna and Rashmika Mandanna as Samskruthi." 
        },
        {
            "movie_id": "15662003",
            "name": "Bharat Ane Nenu",
            "actors": [
                {
                    "actor_id": "15661004",
                    "role":"Chief Minister",
                    "remunration_in_crores":"40"
                }
            ],
            "box_office_collection_in_crores": "500",
            "release_date": "2018-1-14",
            "director_name": "Koratala Siva",
            "avg_rating":"9.2",
            "genre":"Political thriller",
            "budget_in_crores":"100",
            "movie_description":"The film follows Bharat, an Oxford university student who returns to India following the demise of his father, the chief minister of Andhra Pradesh. Disillusioned by the corruption he encounters, Bharat decides to bring about a change in the system after becoming the new chief minister, eventually making enemies." 
        },
        {
            "movie_id": "15662004",
            "name": "Agnyaathavaasi",
            "actors": [
                {
                    "actor_id": "15661006",
                    "role":"Agnyaathavaasi",
                    "remunration_in_crores":"30"
                }
            ],
            "box_office_collection_in_crores": "150",
            "release_date": "2018-4-20",
            "director_name": "Trivikram Srinivas",
            "avg_rating":"5.8",
            "genre":"Action",
            "budget_in_crores":"350",
            "movie_description":"Agnyaathavaasi ( transl. Prince in exile) is a 2018 Indian Telugu-language action film directed by Trivikram Srinivas and starring Pawan Kalyan, with Keerthy Suresh, Anu Emmanuel, Aadhi Pinisetty, Kushboo, and Boman Irani in supporting roles. ... This was Pawan Kalyan's final film before venturing into politics." 
        },
        {
            "movie_id": "15662005",
            "name": "Mirchi",
            "actors": [
                {
                    "actor_id": "15661001",
                    "role":"Hero",
                    "remunration_in_crores":"35"
                },
                {
                    "actor_id": "15661002",
                    "role":"Heroine",
                    "remunration_in_crores":"15"
                }
            ],
            "box_office_collection_in_crores": "450",
            "release_date": "2013-2-8",
            "director_name": "Koratala Siva",
            "avg_rating":"8.4",
            "genre":"Family and Drama",
            "budget_in_crores":"200",
            "movie_description":"Mirchi is a romantic action movie in which, Prabhas, Anushka Shetty and Richa Gangopadhyay are playing the main lead roles. ... Story starts with Jai (Prabhas), who is an architect based in Milan, where he falls in love with Manasa (Richa) at first sight"
         }
    ]


directors_list = [
        {
            "director_id":"15663001",
            "name": "S. S. Rajamouli",
            "age" : "46",
            "base_remuneration_in_crores":"26"
        },
        {
            "director_id":"15663002",
            "name": "Anil Ravipudi",
            "age" : "37",
            "base_remuneration_in_crores":"15"
        },
        {
            "director_id":"15663004",
            "name": "Koratala Siva",
            "age" : "36",
            "base_remuneration_in_crores":"40"
        },
        {
            "director_id":"15663003",
            "name": "Trivikram Srinivas",
            "age" : "48",
            "base_remuneration_in_crores":"35"
        }
    ]
















