from django.shortcuts import render
from .models import Article
# Create your views here.

from django.http import HttpResponse

def index(request):
	return HttpResponse("HELLO AKSHAY STARING SOMETHING NEW FOR OUR PROJECT ")



def article(request):
	article = Article.objects.all()
	return render(request,'article_list.html', {'article':article})
		