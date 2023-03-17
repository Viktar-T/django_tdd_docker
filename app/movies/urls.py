from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("", views.MovieList.as_view()),
    path("<int:pk>/", views.MovieDetail.as_view()),
]
