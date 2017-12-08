"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 08 December, 2017 @ 3:43 PM.
  
  Copyright © 2017. Victor. All rights reserved.
"""
from django import forms


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=255, required=True, name='name')
    matric = forms.CharField(help_text='CSC/2013/001', required=True, name='matric')
    GENDER = (('F', 'female'), ('M', 'male'))
    gender = forms.ComboField(choices=GENDER, name='gender')
    DEPARTMENT = (('ICT', 'Information and Communication Technology'),
                  ('PES', 'Physical and Earth Sciences'),
                  ('BIO', 'Biological Sciences'))
    department = forms.ComboField(choices=DEPARTMENT, name='department')
    LEVEL = (('100', '100 level'), ('200', '200 level'), ('300', '300 level'),
             ('400', '400 level'), ('500', '500 level'))
    level = forms.ComboField(choices=LEVEL, name='level')

    def register(self):
        pass
