"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 28 November, 2017 @ 12:31 PM.
  
  Copyright © 2017. Victor. All rights reserved.
"""

from django.conf.urls import url

from suspects import apps, views

app_name = apps.SuspectsConfig.name

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^(?P<pk>\d+)$', views.Detail.as_view(), name='detail'),
]
