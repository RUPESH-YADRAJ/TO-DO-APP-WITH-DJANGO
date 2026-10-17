from django.urls import path
from . import views

app_name = 'todo'

urlpattern = [
  path('', views.task_list, name = "index"),
  path('/add', views.task_completed, name = 'task_created'),
  path('edit/<int:pk>/', views.task_edited, name = 'task_edited')

]