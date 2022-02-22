from django.db import models
from django.db.models import Avg


class Director(models.Model):
    name = models.CharField(max_length=100)

    @property
    def movies_count(self):
        return self.movies.all().count()


class Movie(models.Model):
    title = models.CharField(max_length=30)
    discription = models.TextField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')

    @property
    def rating(self):
        return Review.objects.filter(movie=self).aggregate(Avg('stars'))

    @property
    def all_reviews(self):
        reviews = Review.objects.filter(movie=self)
        return [{'id': i.id, 'text': i.text} for i in reviews]

    @property
    def count_reviews(self):
        return self.reviews.all().count()

class Review(models.Model):
    stars = models.ImageField(default=5)
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')



