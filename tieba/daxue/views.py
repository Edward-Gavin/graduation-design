# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from daxue import operate
# Create your views here.


def index(request):
    return render(request, 'daxue/index.html')


def catch(request):
    return render(request, 'daxue/catch.html')


def sex(request):
    return render(request, 'daxue/sex.html')


def client(request):
    return render(request, 'daxue/client.html')


def month(request):
    return render(request, 'daxue/month.html')


def hour(request):
    return render(request, 'daxue/hour.html')


def title(request):
    return render(request, 'daxue/title.html')


def post(request):
    return render(request, 'daxue/post.html')


def review(request):
    return render(request, 'daxue/review.html')


def abc(request):
    return render(request, 'daxue/abc.html')


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a)+int(b)
    return HttpResponse(str(c))


def statistic_sex(request):
    """
    Return the number of boys, girls and unknow.

    :return:
    """
    sexes = operate.select_sex_user('user', amount=10000)
    boys = 0
    girls = 0
    unknown = 0
    for sex in sexes:
        for one in sex:
            print(one)
            if str(one) == '女':
                girls += 1
            elif str(one) == '男':
                boys += 1
            else:
                unknown += 1
    result = [girls, boys, unknown]
    return HttpResponse(str(result))


