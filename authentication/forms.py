#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: forms.py
@time: 2020/6/8 16:42
'''

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']