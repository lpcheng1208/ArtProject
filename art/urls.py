# -*- coding: utf-8 -*-
__author__ = 'lpc'
__date__ = '2018/5/29 15:02'

from django.conf.urls import url
from . import index_handler

urlpatterns = [
    url(r'index', index_handler.index, name='index')
]
