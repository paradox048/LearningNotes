from django.urls import path
from . import views


urlPatterns = [
    path('shorten/<str:url>', views.shorten, name='shorten')
]