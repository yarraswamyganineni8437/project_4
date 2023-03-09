from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def yadav(request):
    return HttpResponse('<h1>yadav is a good boy ra naayana</h1>')
def thursday(request):
    return HttpResponse('<h1>thursday saibaba</h1>')
def study(request):
    return HttpResponse('<h1>study hard with positive hope then get job</h1>')
