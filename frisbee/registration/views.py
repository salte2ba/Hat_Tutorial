from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse("Hello and welcome to the Hat Tournament signup!")
