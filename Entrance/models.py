from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class Register(models.Model):
    Gender = [
        ('M','Male'),
        ('F','Female'),
        ('O','Other')
    ]
    id = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=10)
    dob = models.DateField()
    gender = models.CharField(max_length=1,choices=Gender)
    password = models.CharField(max_length=16,validators = [MinLengthValidator(6)])

    def __str__(self):
        return str(self.id)
