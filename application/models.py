from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


# Create your models here.


class Employee(models.Model):
    emp_name = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField()
    image = models.ImageField(upload_to='media/')
    upload_resume = models.FileField(upload_to='documents')

    def __str__(self):
        return self.emp_name
