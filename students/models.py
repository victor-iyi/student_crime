from django.db import models


class Students(models.Model):
    name = models.CharField(max_length=255, name='name')
    gender = models.CharField(max_length=6, name='gender')
    image = models.ImageField(width_field=368, height_field=256, name='image')
    matric = models.CharField(max_length=13, name='matric')
    department = models.CharField(max_length=50, name='department')
    level = models.IntegerField(name='level')

    def __str__(self):
        return f'Students<{self.name}, {self.matric}>'
