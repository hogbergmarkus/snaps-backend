from django.urls import path
from . import views


urlpatterns = [
    path('reports/', views.ReportList.as_view()),
]
