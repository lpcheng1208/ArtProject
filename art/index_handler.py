# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse

__author__ = 'lpc'
__date__ = '2018/5/29 15:03'


def index(request):
    return render(request, 'index.html')
