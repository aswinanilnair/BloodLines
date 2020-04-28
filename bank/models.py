from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # add any additional attributes
    CHOICES = (
        ('A+', 'A +ve'),
        ('B+', 'B +ve'),
        ('AB+', 'AB +ve'),
        ('O+', 'O +ve'),
        ('A-', 'A -ve'),
        ('B-', 'B -ve'),
        ('AB-', 'AB -ve'),
        ('O-','O -ve')
    )

    img = models.ImageField(upload_to='pics',blank=True)
    dob = models.DateField(max_length=8)
    phone = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=3,choices=CHOICES)


    def __str__(self):
        return self.user.username

class BlogPost(models.Model):
    title = models.CharField(max_length = 100)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    blog_img = models.ImageField(upload_to='blog_pics',blank=True)
    desc = models.TextField(max_length=1024)
    created_at = models.DateField(default=datetime.now)

    def __str__(self):
        return self.title


class NewRequest(models.Model):

    CHOICES = (
        ('A+', 'A +ve'),
        ('B+', 'B +ve'),
        ('AB+', 'AB +ve'),
        ('O+', 'O +ve'),
        ('A-', 'A -ve'),
        ('B-', 'B -ve'),
        ('AB-', 'AB -ve'),
        ('O-','O -ve')
    )
    title = models.CharField(max_length = 128,default="Urgent Help")
    name = models.CharField(max_length=128,default="tester")
    msg = models.CharField(max_length = 128)
    phone = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=3,choices=CHOICES)
    email = models.EmailField(max_length=128)
    city = models.CharField(max_length=128,default="Bengaluru")
    #file upload here
    created_at = models.DateField(default=datetime.now)

    def __str__(self):
        return self.msg
