from django.urls import path
from .views import index

urlpatterns = [
    path('polls/', index, name='index')
]