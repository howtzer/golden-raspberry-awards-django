from django.db import models


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField(null=True)
    title = models.CharField(max_length=255, null=True)
    studios = models.CharField(max_length=255, null=True)
    winner = models.CharField(max_length=10, null=True)


class Producer(models.Model):
    id = models.AutoField(primary_key=True)
    producer = models.CharField(max_length=255, null=True)


class Movie_producer(models.Model):
    id = models.AutoField(primary_key=True)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    producer_id = models.ForeignKey(Producer, on_delete=models.CASCADE)
