from django.db import models

# Create your models here.
class student(models.Model):
    id=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=100)
    age=models.IntegerField()
