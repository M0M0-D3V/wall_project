from django.urls import path
from . import views

app_name = 'wall'
urlpatterns = [
    path('', views.wall, name="my_wall"),

    path('', views.message, name="my_message"),

    path('', views.comment, name="my_comment"),

]
