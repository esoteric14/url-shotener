from django.shortcuts import render
from django.http import HttpResponse

def sayhello(req):
    return HttpResponse("hi there")
