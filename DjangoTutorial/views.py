#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: views.py
@time: 2020/6/8 14:49
'''
from django.shortcuts import render


def indexPage(request):
    return render(request,'forum/indexPage.html')