from django.db import models

# Create your models here.

class Department(models.Model):
    name= models.CharField(max_length=70, null=False)
    locals= models.CharField(max_length=70)

class Role(models.Model):
    name= models.CharField(max_length=70, null=False)

class Employee(models.Model):
    firstname= models.CharField(max_length=70, null=False)
    lastname= models.CharField(max_length=70)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.IntegerField(default=0)    