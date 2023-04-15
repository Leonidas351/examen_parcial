from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class userData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    users_role = models.CharField(max_length=32,default='Tipo')
    users_cel_num = models.CharField(max_length=32, default='999888777')
    users_start_date = models.DateField(default=date.today)

class productData(models.Model):
    registered_by = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=32,default='Nombre')
    product_code = models.CharField(max_length=32,default='Apellido')
    price_bought = models.CharField(max_length=50,default='e-mail')
    price_sold = models.CharField(max_length=50,default='e-mail')