from django.db import models

from students.models import Students


# Create your models here.
class Suspects(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    description = models.TextField()
