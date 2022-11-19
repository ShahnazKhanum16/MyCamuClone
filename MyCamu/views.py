from django.shortcuts import render
from django.http import HttpResponse 


# Create your views here.
def home(request):
    return render(request, 'mycamu/main.html')

def Login(request):
    return HttpResponse('WELCOME TO PRECIDENCY UNIVERSITY')

