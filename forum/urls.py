#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: urls.py
@time: 2020/6/8 14:41
'''
from django.urls import path
from . import views

app_name = 'forum'
urlpatterns = [

    path('', views.home, name="home"),
    path('activate/', views.activate, name="activate"),
    path('createThread/', views.create_thread, name="createThread"),
    path('thread/<str:pk>/', views.create_post, name="createPost"),
    path('createComment/<str:pk>/', views.create_comment, name="createComment"),
    path('profile/<str:pk>/', views.profile, name="profile"),


]