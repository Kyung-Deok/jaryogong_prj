from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def home(request) :
    return JsonResponse({"h" : "hello world"})

def change_user(request):
    pass

def vouchers(request):
    pass

def rent_tops(request):
    pass

def events(request):
    request