from django.urls import path
from . import views

app_name = 'wall'
urlpatterns = [
    path('', views.wall, name="my_wall"),

    path('new_message', views.new_message, name="my_new_message"),

    path('wall', views.this_message, name="my_this_message"),

    path('', views.comment, name="my_comment"),

]
