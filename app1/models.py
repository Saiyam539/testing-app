from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todos(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    task = models.CharField(max_length=20)
    desc = models.TextField(max_length=50)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.task
    
    class Meta:
        ordering = ['complete'] 