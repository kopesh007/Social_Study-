from django.db import models


class Pdfs(models.Model):
    subject=models.CharField(max_length=50)
    topic=models.CharField(max_length=200)
    contain=models.CharField(max_length=300)
    file=models.FileField(upload_to='pdf/')

    def __str__(self):
        return f"{self.subject} --> {self.topic}"
# Create your models here.

class model_QA(models.Model):
    subject=models.CharField(max_length=50)
    topic=models.CharField(max_length=200)
    contain=models.CharField(max_length=300)
    file=models.FileField(upload_to='model_QA/')

    def __str__(self):
        return f"{self.subject} --> {self.topic}"
