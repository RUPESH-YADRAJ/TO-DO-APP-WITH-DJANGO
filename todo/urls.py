from django.urls import path
from . import views

app_name = 'todo'

urlpattern = [
  path('', views.task_list, name = "index"),
  path('/add', views.task_create, name = 'task_create'),
  path('edit/<int:pk>/', views.task_update, name = 'task_update'),
  path('delete/<int:pk>/', views.task_delte, name = 'task_delete'),
  path('toggle/<int:pk>/', views.task_toggle_complete, name = 'task_toggle_complete')

]