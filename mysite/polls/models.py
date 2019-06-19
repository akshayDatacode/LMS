from django.db import models

class Article(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class StudentData(models.Model):
	student_name = models.CharField(max_length=40)
	email_address = models.EmailField(max_length=100)
	student_password = models.CharField(max_length=20)
	

	def __str__(self):
		return self.student_name
		