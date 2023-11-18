from django.urls import path
from . import views

# URLConfg
urlpatterns = [
    path('hello/',views.say_hello)
]