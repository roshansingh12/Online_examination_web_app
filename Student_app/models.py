from django.db import models

# Create your models here.
class test_score(models.Model):
    test_name=models.CharField(max_length=300)
    student_email=models.CharField(max_length=300)
    wrong_ans=models.IntegerField()
    right_ans=models.IntegerField()
    test_status=models.BooleanField()
    total_marks=models.IntegerField()
    score_obtained=models.IntegerField()
    test_class=models.CharField(max_length=100)
class test_status(models.Model):
    test_name=models.CharField(max_length=300)
    student_email=models.CharField(max_length=300)
    test_status=models.BooleanField()
