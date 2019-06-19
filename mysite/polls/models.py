from django.db import models

class Article(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
