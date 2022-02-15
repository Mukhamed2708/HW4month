from rest_framework import serializers
from movie.models import Movie, Review, Director


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name'.split()

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'title discription director'.split()
        # fields = '__all__'

