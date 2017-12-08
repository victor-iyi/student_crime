"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 28 November, 2017 @ 12:31 PM.
  
  Copyright © 2017. Victor. All rights reserved.
"""

from django.urls import path

from suspects import apps, views

app_name = apps.SuspectsConfig.name

urlpatterns = [
    path(r'', views.Index.as_view(), name='index'),
    path(r'<int:suspect_id>/', views.Detail.as_view(), name='detail'),
]
