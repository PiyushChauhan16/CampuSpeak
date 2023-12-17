from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.login, name = "login"),
    path ("index/", views.index, name = "index"),
    path ("fullPost/", views.fullPost, name = "fullPost"),
    path ("commentReply/", views.commentReply, name = "commentReply")
]