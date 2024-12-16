from django.db import models

class todolist(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True,null=True)
    status = models.BooleanField(default=False)  # Corrected 'defult' to 'default'
