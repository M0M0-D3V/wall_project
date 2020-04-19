from django.urls import path
from . import views
urlpatterns = [
    path('', views.wall, name="my_wall"),

]
