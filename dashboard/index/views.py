from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def home() :
    return JsonResponse({"h" : "hello world"})
