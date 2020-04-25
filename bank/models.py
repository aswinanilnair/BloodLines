from django.db import models
from django.contrib.auth.models import User

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
