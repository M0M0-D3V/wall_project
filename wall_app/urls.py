from django.urls import path
from . import views

app_name = 'wall'
urlpatterns = [
    path('', views.index, name="my_index"),

    path('new_message', views.new_message, name="my_new_message"),

    path('wall', views.this_message_on_wall, name="my_this_message_on_wall"),

    path('new_comment', views.new_comment, name="my_new_comment"),

    # path('delete_message', views.delete_message, name="my_delete.message"),


]
