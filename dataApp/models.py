from django.db import models

# Create your models here.

class Student(models.Model):
    studentName = models.CharField(max_length = 30)
    studentId = models.IntegerField()
    studentClass = models.IntegerField()
    studentAddress = models.CharField(max_length = 150)


# python manage.py sqlmigrate dataApp 0001

"""
Here dataApp is the name of your App of your project

0001 is genertated automatically by django at the time of migration

"""