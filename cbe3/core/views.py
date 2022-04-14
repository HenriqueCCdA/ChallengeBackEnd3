# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(resquet):
    return HttpResponse('Olá mundo')
