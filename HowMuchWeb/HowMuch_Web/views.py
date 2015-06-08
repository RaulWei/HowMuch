from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def qScore(request):
    return HttpResponse('qScore')

def qCourse(request):
    return HttpResponse('qCourse')