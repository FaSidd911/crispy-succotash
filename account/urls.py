from django.contrib import admin
from django.urls import path
from account import views

urlpatterns = [
    path("", views.index, name='home'),
    path("addSociety", views.addSociety, name='addSociety'),
    path("contact", views.contact, name='contact'),
    path("login", views.login, name='login'),
]