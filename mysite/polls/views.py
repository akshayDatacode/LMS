from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
	return HttpResponse("HELLO AKSHAY STARING SOMETHING NEW FOR OUR PROJECT ")