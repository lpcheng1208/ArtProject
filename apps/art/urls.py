# -*- coding: utf-8 -*-
from art import search_handler, index_handler, detail_handler

__author__ = 'lpc'
__date__ = '2018/5/29 15:02'

from django.conf.urls import url

urlpatterns = [
    url(r'index', index_handler.IndexHandler, name='index'),
    url(r'search', search_handler.SearchHandler, name='search'),
    url(r'detail', detail_handler.DetailHandler, name='search'),
]
