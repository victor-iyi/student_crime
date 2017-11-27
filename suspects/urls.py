"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 27 November, 2017 @ 1:42 PM.
  
  Copyright © 2017. Victor. All rights reserved.
"""

from django.conf.urls import url
from . import apps, views


app_name = apps.SuspectsConfig.name

urlpatterns = [
    url(r'^$', views.SuspectsAll.as_view(), name='index'),
    url(r'^(?P<pk>\d+)$', views.SuspectsDetail.as_view(), name='detail'),
]
