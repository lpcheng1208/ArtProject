import math

from django.shortcuts import render
from .models import UserMessage


def MessageSubmit(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        message = request.POST.get('message', '')
        user_mes = UserMessage()
        user_mes.name = name
        user_mes.email = email
        user_mes.address = address
        user_mes.message = message
        user_mes.save()
        UserMsgs = UserMessage.objects.all()
        total = UserMsgs.count()
        shownum = 10
        pagenum = int(math.ceil(total / shownum))

        data = UserMsgs
        print(data)
        btnum = 5
        firtpage = 1
        lastpage = pagenum
        context = dict(
            pagenum=pagenum,
            total=total,
            prev=1,
            next=1,
            pagerange=range(1, 2),
            data=data,
            url=request.path,
            page=1,
        )
        return render(request, 'msg_list.html', context=context)
    return render(request, 'msg_form.html')


def msg_info(request):
    UserMsgs = UserMessage.objects.all()
    data = UserMsgs
    cont = dict(
        data=data
    )
    return render(request, 'msg_list.html', cont)
