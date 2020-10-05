from django.db import models

# Create your models here.
class Class(models.Model):
    class_name=models.CharField(max_length=300)
class teacher(models.Model):
    teacher_name=models.CharField(max_length=300)
    teacher_email=models.CharField(max_length=300)
    class1=models.CharField(max_length=300)
    class2=models.CharField(max_length=300)
    class3=models.CharField(max_length=300)
    class4=models.CharField(max_length=300)
    class5=models.CharField(max_length=300)
class student(models.Model):
    student_name=models.CharField(max_length=300)
    student_email=models.CharField(max_length=300)
    student_class=models.CharField(max_length=300)
    
