from django.urls import path
from ecom_website import views
from . import views


app_name = "ecom_website"

urlpatterns = [
    path("", views.home, name="home"),
    path("search", views.search, name="search"),
    path("search/<str:pk>/", views.details, name="details"),
    path('create', views.create, name='create'),
]