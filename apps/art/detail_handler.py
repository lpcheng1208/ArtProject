# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render

from art.models import Art

__author__ = 'lpc'
__date__ = '2018/5/29 20:53'


def DetailHandler(request):
    print('DetailHandler#enter!')
    # id = self.get_argument("id", None)
    id = request.GET.get("id", None)
    print('DetailHandler#id:' + str(id))
    if id == None:
        return HttpResponseRedirect("/art/index")
    else:
        art = Art.objects.get(id=int(id))
        context = {"art": art}
        return render(request, "home/detail.html", context=context)
