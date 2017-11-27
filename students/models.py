from django.db import models


class Students(models.Model):
    name = models.CharField(max_length=255, name='name')
    matric = models.CharField(max_length=13, name='matric')
    gender = models.CharField(max_length=6, name='gender')
    level = models.IntegerField(name='level')

    def __str__(self):
        return f'Students<{self.name}, {self.matric}>'
