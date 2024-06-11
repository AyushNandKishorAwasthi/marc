from django.db import models
#step 1 model banao
#step 2 model ko admin me register karo fir ye step 3 and step 4 ki command run karo 
#step 3 command python manage.py makemigrations
#step 4 command python manage.py migrate 

class Enquiry(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    emailaddress = models.CharField(max_length=50)
    subject = models.CharField(max_length=500)
    message = models.CharField(max_length=5000)
    posteddate = models.CharField(max_length=30)

class Customer(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    address = models.CharField(max_length=500)
    contactno = models.CharField(max_length=10)
    emailaddress = models.CharField(max_length=50,primary_key=True)
    regdate = models.CharField(max_length=30)

class Login(models.Model):
    userid = models.CharField(max_length = 50, primary_key = True)
    password = models.CharField(max_length = 30)
    usertype = models.CharField(max_length = 30)
