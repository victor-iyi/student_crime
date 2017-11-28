from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=255, name='name')
    GENDER = (('F', 'female'), ('M', 'male'))
    gender = models.CharField(max_length=1, choices=GENDER, name='gender')
    image = models.ImageField(width_field=368, height_field=256, name='image')
    matric = models.CharField(max_length=13, name='matric')
    department = models.CharField(max_length=50, name='department')
    LEVEL = (('100', '100 level'), ('200', '200 level'), ('300', '300 level'),
             ('400', '400 level'), ('500', '500level'))
    level = models.CharField(max_length=3, choices=LEVEL, name='level')

    def __str__(self):
        return f'<{self.name}, {self.matric}>'
