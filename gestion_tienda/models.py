from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32,default='Nombre')
    last_name = models.CharField(max_length=32,default='Apellido')
    e_mail = models.CharField(max_length=50,default='e-mail')
    username = models.CharField(max_length=32,default='Username')
    password = models.CharField(max_length=32,default='Password')
    role = models.CharField(max_length=32,default='Cargo')
    cel_num = models.CharField(max_length=32, default='999888777')
    start_date = models.DateField(default=date.today)

class Producto(models.Model):
    product_name = models.CharField(max_length=32,default='Nombre')
    product_code = models.CharField(max_length=32,default='Apellido')
    price_bought = models.CharField(max_length=50,default='e-mail')
    price_sold = models.CharField(max_length=50,default='e-mail')
    #registered_by = models.ForeignKey()