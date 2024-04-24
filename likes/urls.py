from django.urls import path
from . import views


urlpatterns = [
    path('likes/', views.LikeList.as_view()),
]
