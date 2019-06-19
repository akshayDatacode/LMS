from django.shortcuts import render
from .models import Article
from .models import StudentData
# Create your views here.

from django.http import HttpResponse

def index(request):
	return HttpResponse("HELLO AKSHAY STARING SOMETHING NEW FOR OUR PROJECT ")



def article(request):
	article = Article.objects.all()
	return render(request,'article_list.html', {'article':article})

def student_data(request):
	student_data = StudentData.objects.all()
	return render(request,'student_data.html', {'studentdata':student_data})
		