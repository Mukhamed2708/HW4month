from django.contrib import admin
from django.urls import path
from movie import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/movies/', views.movie_list_view),
    path('api/v1/movies/<int:id>/', views.movie_detail_view),
    path('api/v1/reviews/', views.review_list_view),
    path('api/v1/reviews/<int:id>/', views.get_review),
    path('api/v1/director/', views.director_list_view),
    path('api/v1/director/<int:id>/', views.get_director),

]
