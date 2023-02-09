from django.db import models

# Create your models here.
from django.db import models

#Member model to store the member info in DB
class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    CHOICES = [
        ('Admin', 'Admin'),
        ('General', 'General'),
    ]
    role = models.CharField(
        choices=CHOICES, max_length=100, default='Admin')


def __str__(self):
    return self.first_name