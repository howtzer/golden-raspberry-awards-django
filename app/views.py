from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MovieSerializer
from .utils import get_produtores_premiados, RESPONSE_GET, atualiza_segundo_valor, atualiza_response

from .models import Movie, Producer, Movie_producer

# Create your views here.

class movies_list(APIView):

    def get(self, request):

        intervalos = get_produtores_premiados()
        minIntervals = [9999, 9999]
        maxIntervals = [0, 0]
        response = RESPONSE_GET
        
        print(intervalos)

        for i in intervalos:
            if all(i["intervalos"]["maxInterval"] > interval for interval in maxIntervals):
                if i["intervalos"]["maxInterval"] > maxIntervals[0]:
                    atualiza_segundo_valor(response, operacao="max")
                    maxIntervals[0] = i["intervalos"]["maxInterval"]
                    atualiza_response(response, indice=0, intervalo=i, operacao="max")

            if all(i["intervalos"]["minInterval"] < interval for interval in minIntervals):
                if i["intervalos"]["minInterval"] < minIntervals[0]:
                    atualiza_segundo_valor(response, operacao="min")
                    minIntervals[0] = i["intervalos"]["minInterval"]
                    atualiza_response(response, indice=0, intervalo=i, operacao="min")

        return Response(response, status=status.HTTP_200_OK)


class movies_detail(APIView):

    def get(self, request, id=None):
        movies = Movie.objects.filter(id=id)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    def delete(self, request, id=None):
        movie = Movie.objects.filter(id=id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def put(self, request, id=None):
        movies = Movie.objects.filter(id=id)
        serializer = MovieSerializer(movies, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

