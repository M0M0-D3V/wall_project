from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="my_index"),

    path('register', views.register, name="my_register"),

    path('login', views.login, name="my_login"),

    path('success', views.success, name="my_success"),

    path('logout', views.logout, name="my_logout"),

]
