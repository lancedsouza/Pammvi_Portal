from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone1=models.IntegerField()
  phone2=models.IntegerField()
  application_date=models.DateField()
  city=models.CharField(max_length=255)
  state=models.CharField(max_length=255)
  email_id=models.CharField(max_length=255)
  job_applied_for=models.CharField(max_length=255)
  age=models.IntegerField()




# Create your models here.
