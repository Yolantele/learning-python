from django.shortcuts import render
from django.http import HttpResponse

# creates one view
def home(request):
    return HttpResponse('Hello, World!')