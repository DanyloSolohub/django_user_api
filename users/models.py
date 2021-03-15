from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator


# Create your models here.

class UserModel(models.Model):
    class Meta:
        db_table = 'users'
        verbose_name = 'User'

    name = models.CharField(max_length=20, validators=[
        RegexValidator('^[a-zA-z]{2,20}$', 'name must be only a-z A-Z and min 2 max 20 characters')])
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(150)])
    gender = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
