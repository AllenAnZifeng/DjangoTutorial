#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: froms.py
@time: 2020/6/10 14:22
'''

from django.forms import ModelForm
from .models import Threads,Posts,Comments,ForumUser


class ForumUserForm(ModelForm):
    class Meta:
        model = ForumUser
        fields = '__all__'

class ThreadForm(ModelForm):
    class Meta:
        model = Threads
        fields = ['title','content']


class PostForm(ModelForm):
    class Meta:
        model = Posts
        # fields ='__all__'
        fields = ['content']


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        # fields ='__all__'
        fields = ['content']