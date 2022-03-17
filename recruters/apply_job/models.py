from django.db import models

# Create your models here.


class Job_seeker(models.Model):
    name = models.CharField(max_length=300)
    DOB = models.DateField()
    qualification = models.CharField(max_length=1000)
    contact = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=300)


class College(models.Model):
    name = models.CharField(max_length=300)
    branch = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    state = models.CharField(max_length=300)
    email = models.EmailField()


class Staff(models.Model):
    staff_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    DOB = models.DateField()
    qualification = models.CharField(max_length=1000)
    designation = models.CharField(max_length=300)
    college_name = models.ForeignKey(College, on_delete=models.CASCADE)
