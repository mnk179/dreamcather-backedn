from django.urls import path

from . import views

urlpatterns = [
    path('user/create', views.create_user, name='create_user'),
    path('user/login', views.login, name='login'),
]
