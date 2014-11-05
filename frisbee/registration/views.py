from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse("Hello and welcome to the Hat Tournament signup!")
def signup (request):
	return HttpResponse("This is where you will sign up")
def thanks (request):
	return HttpResponse("Thank you for signing up!")	

