from django.apps import AppConfig
from copy import deepcopy
from .utils import load_movies_csv



class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        from .models import Movie, Producer, Movie_producer

        #limpa o banco de dados
        Movie.objects.all().delete()
        Producer.objects.all().delete()
        Movie_producer.objects.all().delete()

        movie_list_dict = load_movies_csv()

        #alimenta o banco de dados
        for i in movie_list_dict:
            movie = Movie()
            movie.year = i["year"]
            movie.title = i["title"]
            movie.studios = i["studios"]
            movie.winner = i["winner"]
            movie.save()
            
            producers = i["producers"].replace(", and", ", ")
            producers = producers.replace(" and ", ", ")
            producers = producers.split(", ")

            for prod in producers:
                producer, created = Producer.objects.update_or_create(
                    producer = prod.strip()
                )

                Movie_producer.objects.create(
                    movie_id = movie,
                    producer_id = producer
                )

        return movie_list_dict