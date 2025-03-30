from django.db import models
from myapp.models import Student
#from django.db import models

# Create your models here.
class Student(models.Model): #in parameter passed parent class so it can use the features of parent class.
    name=models.CharField(max_length=200)
    college=models.CharField(max_length=200)
    age=models.IntegerField()
    is_active=models.BooleanField(default=False)