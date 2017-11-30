from django.core.files.storage import FileSystemStorage
from django.db import models

from students.apps import StudentsConfig

fs = FileSystemStorage(location='public/static/')


class Student(models.Model):
    # student's identification
    name = models.CharField(max_length=255, name='name')
    matric = models.CharField(max_length=13, name='matric')
    # student's gender
    GENDER = (('F', 'female'), ('M', 'male'))
    gender = models.CharField(max_length=1, choices=GENDER, name='gender')
    # student's department
    DEPARTMENT = (('ICT', 'Information and Communication Technology'),
                  ('PES', 'Physical and Earth Sciences'),
                  ('BIO', 'Biological Sciences'))
    department = models.CharField(max_length=50, choices=DEPARTMENT, name='department')
    # student's level
    LEVEL = (('100', '100 level'), ('200', '200 level'), ('300', '300 level'),
             ('400', '400 level'), ('500', '500 level'))
    level = models.CharField(max_length=10, choices=LEVEL, name='level')
    # Student's image
    UPLOAD_PATH = f'images/{StudentsConfig.name}'
    image = models.ImageField(storage=fs, upload_to=UPLOAD_PATH, default='', name='image')

    def __str__(self):
        return f'{self.name}, {self.matric}'
