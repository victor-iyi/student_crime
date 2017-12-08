"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 28 November, 2017 @ 12:24 PM.
  
  Copyright © 2017. Victor. All rights reserved.
"""
from django.urls import path
from students import apps, views

app_name = apps.StudentsConfig.name

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('<int:student_id>/', views.Detail.as_view(), name='detail'),
    # Student CRUD
    path('register/', views.StudentCreate.as_view(), name='student-register'),
    path('<int:pk>/', views.StudentUpdate.as_view(), name='student-update'),
    path('<int:pk>/delete/', views.StudentDelete.as_view(), name='student-delete'),
]
