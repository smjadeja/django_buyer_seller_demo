from django.db import models
from datetime import date, datetime
from django import forms
from .widget import DatePickerInput,DateTimePickerInput,TimePickerInput
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _

class CustomMinvalue(MinValueValidator):
    message = _("Please positive value.")

class User_Role(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    role_name = models.CharField(max_length=20)       
    role_desc = models.CharField(max_length=20)

    def __str__(self):
        return self.role_name.capitalize()

class MyUser(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=30)
    dob = models.DateField(verbose_name='Date of birth', null=True)
    email = models.EmailField(unique=True)
    mobile = models.IntegerField()
    balance = models.FloatField(validators=[CustomMinvalue(0), MaxValueValidator(100000)])
    password = models.CharField(max_length=10)
    address = models.TextField(max_length=100)
    user_role = models.ForeignKey(User_Role, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
        
class Product(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    product_name = models.CharField(max_length=20)
    product_desc = models.CharField(max_length=100)
    product_img = models.ImageField(upload_to='images/')
    prod_sell_price = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100000)])
    prod_cost_price = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100000)])
    stock_unit = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    created_by_user = models.ForeignKey(MyUser, null=True, on_delete=models.SET_NULL)
    created_date = models.DateField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name

class User_Purchase(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    purchase_date = models.DateField(auto_now_add=True)
    product_id =  models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
    total_unit = models.IntegerField()
    purchased_by_user = models.ForeignKey(MyUser, related_name='purchased_by_user', null=True, on_delete=models.SET_NULL)
    purchased_from_user = models.ForeignKey(MyUser, related_name='purchased_from_user',  null=True, on_delete=models.SET_NULL)


    
