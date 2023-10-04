from django.urls import path
from musician.views import Home

urlpatterns = [
    path('home', Home.as_view(), name='home'),
]

