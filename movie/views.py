from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movie.models import Movie, Review, Director
from movie.serializers import MovieSerializer, ReviewListSerializer, DirectorSerializer, MovieReviewSerializer

@api_view(['GET'])
def movie_reviews_view(request):
    product = Movie.objects.all()
    data = MovieReviewSerializer(product, many=True).data
    return Response(data=data)

@api_view(['GET'])
def movie_list_view(request):
    products = Movie.objects.all()
    data = MovieSerializer(products, many=True).data
    return Response(data=data)

@api_view(['GET'])
def movie_detail_view(request, id):
    try:
        product = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'massage': 'Product not found'})
    data = MovieSerializer(product).data
    return Response(data=data)


@api_view(['GET'])
def review_list_view(request):
    movies = Review.objects.all()
    data = ReviewListSerializer(movies, many=True).data
    return Response(data=data)


@api_view(['GET'])
def get_review(request, id):
    try:
        movies = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'message': 'REVIEW not found'}, status=status.HTTP_404_NOT_FOUND)
    data = ReviewListSerializer(movies).data
    return Response(data=data)


@api_view(['GET'])
def director_list_view(request):
    movie = Director.objects.all()
    data = DirectorSerializer(movie, many=True).data
    return Response(data=data)


@api_view(['GET'])
def get_director(request, id):
    try:
        movie = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'message': 'DIRECTOR not found'}, status=status.HTTP_404_NOT_FOUND)
    data = DirectorSerializer(movie).data
    return Response(data=data)

