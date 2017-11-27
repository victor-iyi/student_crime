from django.db import models


class Students(models.Model):
    name = models.CharField(max_length=255, name='name')
    matric = models.CharField(max_length=13, name='matric')
    gender = models.BinaryField(choices=['male', 'female'], name='gender')
    level = models.IntegerField(name='level')

    def __str__(self):
        return f'Students<{self.name}, {self.matric}>'


class Suspects(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    description = models.TextField()
