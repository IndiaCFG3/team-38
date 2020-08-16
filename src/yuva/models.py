from django.db import models# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
  name = models.CharField(max_length=150)
  email = models.EmailField(blank=True)
  address = models.CharField(max_length=50)
  phone = models.CharField(max_length=150,unique=True)
  profile = models.TextField()    
  def __str__(self):
      return self.name

class Support_Team(models.Model):
  candidate_id = models.CharField(max_length = 50)
  name = models.CharField(max_length = 100)
  email = models.EmailField(blank=True)
  batch_id = models.IntegerField()
  enrolled_course = models.CharField(max_length = 50)
  enrolled_date = models.CharField(max_length=50)
  attendance = models.FloatField()
  course_status = models.CharField(max_length=50)
  placement_status = models.CharField(max_length=50)
  
  def __str__(self):
    return self.name

class Audit(models.Model):
  center_id = models.CharField(max_length = 50)
  city = models.CharField(max_length = 100)
  student_count = models.IntegerField()
  staff_count = models.IntegerField()
  students_joined = models.IntegerField()
  students_completed = models.IntegerField()
  students_dropped = models.IntegerField()
  rating = models.IntegerField()
  
  def __str__(self):
    return self.center_id

class HR(models.Model):
  employee_id = models.CharField(max_length=50)
  employee_name = models.CharField(max_length=150)
  employee_phone = models.CharField(max_length=150,unique=True)
  employee_email = models.EmailField(blank=True)
  manager_id = models.IntegerField()
  doj = models.CharField(max_length=50)
  employee_status = models.CharField(max_length=50)
  leaves_applied = models.IntegerField()  
  def __str__(self):
      return self.employee_name