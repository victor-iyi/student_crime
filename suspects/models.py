from django.db import models

from students.models import Student


# Create your models here.
class Suspect(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    description = models.TextField()
