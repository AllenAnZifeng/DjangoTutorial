#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: url.py.py
@time: 2020/5/10 13:44
'''


from django.urls import path

from . import views

app_name = 'polls' # namespace
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('<int:pk>/',views.DetailView.as_view(),name='detail'),
    path('<int:pk>/results/',views.ResultsView.as_view(),name='results'),
    path('<int:question_id>/vote',views.vote,name='vote'),
    path('error',views.error,name='error'),
    path('parent',views.parent,name='parent'),
    path('child',views.child,name='child'),
]