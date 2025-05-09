from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "main/index.html")


def about(request):
    context = {
        'author_FIO': 'Селюжицкий Иван Павлович',
        'BIO':'группа: 81 ТП',
        'LR':'лабораторная №14'
    }
    return render(request, "main/about.html", context)


def shop(request):
    context = {
        'shop_name': 'Магазин тематических кружек и термосов'
    }
    return render(request, "main/shop.html", context)
