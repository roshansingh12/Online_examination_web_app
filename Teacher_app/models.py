from django.db import models

# Create your models here.

class test(models.Model):
    test_name=models.CharField(max_length=100,unique=True)
    test_class=models.CharField(max_length=100)
    test_teacher=models.CharField(max_length=100)
class ques(models.Model):
    question=models.CharField(max_length=100)
    op1=models.CharField(max_length=100)
    op2=models.CharField(max_length=100)
    op3=models.CharField(max_length=100)
    op4=models.CharField(max_length=100)
    cop=models.CharField(max_length=100)
    test_name=models.CharField(max_length=100)
    marks=models.IntegerField()
