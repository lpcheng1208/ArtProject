# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render

from art.models import Art

__author__ = 'lpc'
__date__ = '2018/5/29 20:53'

from Django_New.settings import logger


def DetailHandler(request):
    # logger.info("IndexHandler request Handler begin")
    id = request.GET.get("id", None)
    # logger.debug('query total:' + str(id))
    if id == None:
        return HttpResponseRedirect("/art/index")
    else:
        art = Art.objects.get(id=int(id))
        context = {"art": art}
        # logger.info("IndexHandler request Handler end")
        return render(request, "home/detail.html", context=context)
