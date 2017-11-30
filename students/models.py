from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=255, name='name')
    matric = models.CharField(max_length=13, name='matric')
    GENDER = (('F', 'female'), ('M', 'male'))
    gender = models.CharField(max_length=1, choices=GENDER, name='gender')
    DEPARTMENT = (('ICT', 'Information and Communication Technology'),
                  ('PES', 'Physical and Earth Sciences'),
                  ('BIO', 'Biological Sciences'))
    department = models.CharField(max_length=50, choices=DEPARTMENT, name='department')
    LEVEL = (('100', '100 level'), ('200', '200 level'), ('300', '300 level'),
             ('400', '400 level'), ('500', '500 level'))
    level = models.CharField(max_length=10, choices=LEVEL, name='level')
    image = models.ImageField(width_field=368, height_field=256, name='image')

    def __str__(self):
        return f'{self.name}, {self.matric}'
