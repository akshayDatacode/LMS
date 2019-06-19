from django.shortcuts import render

from django.http import HttpResponse

def stdlogin(request):
	return HttpResponse("WEll come to Student Login ")