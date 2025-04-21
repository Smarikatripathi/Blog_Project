from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),  # Add this line for the index view
]


