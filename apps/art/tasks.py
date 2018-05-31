# -*- coding: utf-8 -*-
__author__ = 'lpc'
__date__ = '2018/5/31 14:30'

from celery import Celery
from time import sleep

# broker="redis://redis:6379/1" 列队数据库存放点
# backend="redis://redis:6379/2" 任务执行完成后数据库存放点

from Django_New.celery import app


@app.task
def add(x, y):
    return x + y


@app.task
def mult(x, y):
    sleep(10)
    return x * y


@app.task
def getname(name):
    return name

