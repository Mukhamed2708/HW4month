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


@api_view(['GET', 'POST'])
def movie_list_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data = MovieSerializer(movies, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        # product = Product.objects.create(**request.data)
        print(request.data)
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        category_id = request.data.get('category_id')
        movies = Movie.objects.create(title=title, description=description,
                                         price=price, category_id=category_id)
        return Response(data=MovieSerializer(movies).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'massage': 'Product not found'})
    if request.method == 'GET':
        data = MovieSerializer(movie).data
        return Response(data=data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.price = request.data.get('price')
        movie.category_id = request.data.get('category_id')
        movie.save()
        return Response(data=MovieSerializer(movie).data)


@api_view(['GET', 'POST'])
def review_list_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewListSerializer(reviews, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        # product = Product.objects.create(**request.data)
        print(request.data)
        stars = request.data.get('stars')
        text = request.data.get('text')
        movie = request.data.get('movie')
        reviews = Review.objects.create(stars=stars, text=text,
                                         movie=movie)
        return Response(data=ReviewListSerializer(reviews).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def get_review(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'massage': 'Product not found'})
    if request.method == 'GET':
        data = ReviewListSerializer(review).data
        return Response(data=data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        review.stars = request.data.get('stars')
        review.text = request.data.get('text')
        review.movie = request.data.get('movie')
        review.save()
        return Response(data=ReviewListSerializer(review).data)


@api_view(['GET', 'POST'])
def director_list_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        data = DirectorSerializer(directors, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        # product = Product.objects.create(**request.data)
        print(request.data)
        name = request.data.get('name')
        directors = Director.objects.create(name=name)
        return Response(data=DirectorSerializer(directors).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def get_director(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'massage': 'Product not found'})
    if request.method == 'GET':
        data = DirectorSerializer(director).data
        return Response(data=data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        director.name = request.data.get('name')
        director.save()
        return Response(data=DirectorSerializer(director).data)
