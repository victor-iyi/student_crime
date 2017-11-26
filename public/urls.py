"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 26 November, 2017 @ 1:25 PM.
  
  Copyright © 2017. Victor. All rights reserved.
"""
from django.conf.urls import url
from . import views, apps

app_name = apps.PublicConfig.name

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^contact/$', views.contact, name='contact')
]
