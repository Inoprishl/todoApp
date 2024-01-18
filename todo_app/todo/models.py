from django.db import models

# Create your models here.

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    status = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-id']
    
    def __str__(self):
        return self.title
    