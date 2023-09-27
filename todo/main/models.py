
# Create your models here.
from django.db import models

class Task(models.Model):
    task = models.CharField(max_length=255)  # or TextField, depending on your needs
    # Other fields in your model
    is_completed=models.BooleanField(default=False)
    created_date=models.DateField(auto_now_add=True)
    update_date=models.DateField(auto_now=True)
