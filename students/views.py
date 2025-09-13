from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def students(request):
    l=[{1:2,4:5}]
    return HttpResponse(l)