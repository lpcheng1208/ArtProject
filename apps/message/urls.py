# -*- coding: utf-8 -*-
from django.conf.urls import url

__author__ = 'lpc'
__date__ = '2018/5/31 19:39'
from .views import MessageSubmit, msg_info

urlpatterns = [
    url(r'^$', MessageSubmit, name='go_form'),
    url(r'msg_info', msg_info, name='msg_info'),
]
