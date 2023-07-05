from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    emailid = models.EmailField(max_length=30, default="")
    # mobile = models.CharField(max_lenght=15)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username

# this model is for Hiring form
class hiringForm(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email_id = models.CharField(max_length=50)
    Shift = models.CharField(max_length=50)
    ContactNo = models.CharField(max_length=50)
    Gender = models.CharField(max_length=50)
    NumberOfGuard = models.CharField(max_length=50)


    def  __str__(self):
        return self.firstName



class Contact(models.Model):
    username=models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Description = models.CharField(max_length=500)

    def  __str__(self):
        return self.username