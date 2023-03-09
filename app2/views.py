from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def yadav(request):
    return HttpResponse('<marquee><h1>yadav is a honest boy</h1></marquee>')
def pythonmock(request):
    return HttpResponse('<marquee><h1>saturday iam giving python mock</h1></marquee>')
def job(request):
    return HttpResponse('<marquee><h1>job is require for me </h1></marquee>')
