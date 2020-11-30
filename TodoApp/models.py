from django.db import models

class TodoApp(models.Model):
   text = models.CharField(max_length=20)
   completed = models.BooleanField(default=False)

   def __str__(self):
       return self.text 
