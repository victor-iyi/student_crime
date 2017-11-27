"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 26 November, 2017 @ 1:19 PM.
  
  Copyright © 2017. Victor. All rights reserved.
"""
from django.conf.urls import url
from . import apps, views

app_name = apps.StudentsConfig.name

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^all$', views.StudentsAll.as_view(), name='all'),
    url('^suspects$', views.SuspectsAll.as_view(), name='suspects'),
]
