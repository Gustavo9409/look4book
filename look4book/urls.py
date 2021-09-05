from django.urls import path
from . import views

# Urls of the project
urlpatterns = [
    path('Home/', views.initHome, name='Home'),
     path('Results/', views.showResults, name='Results'),
]
