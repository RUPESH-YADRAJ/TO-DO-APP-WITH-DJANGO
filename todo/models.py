from django.db import models

# Create your models here.
class Task(models.model):
  title = models.TextField(blank = True)
  description = models.TextField(blank = True)
  completed = models.BooleanField(default = False)
  created_at = models.DateTimeField(auto_now_add = True)

  def __str__(self):
    return self.title