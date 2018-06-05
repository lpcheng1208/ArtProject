import json

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# def index(request):
#     return render(request, "home/index.html")


def add_handler(request):
    x = request.POST.get('x', '1')
    y = request.POST.get('y', '1')
    #from .tasks import add
    #add.delay(int(x), int(y))
    res = {'code': 200, 'message': 'ok', 'data': [{'x': x, 'y': y}]}
    return HttpResponse(json.dumps(res))


