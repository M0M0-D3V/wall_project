from django.urls import path
from . import views

app_name = 'wall'
urlpatterns = [
    path('', views.wall, name="my_wall"),

]
