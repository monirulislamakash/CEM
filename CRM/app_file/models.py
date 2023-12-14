from django.db import models
from datetime import datetime
# Create your models here.
class Customur(models.Model):
    Name=models.CharField(max_length=100)
    Phone=models.CharField(max_length=30)
    Email=models.CharField(max_length=100)
    Image=models.FileField(upload_to="media/profile/images",default="static/img/avatars/profile_avter.webp")
    Adress=models.CharField(max_length=300, default="not available")
    Block=models.BooleanField(default=False)
    Delete=models.BooleanField(default=False)
    def __str__(self):
        return self.Name+" | "+self.Phone
class ProductPrice(models.Model):
    Product_Name=models.CharField(max_length=100)
    Image=models.FileField(upload_to="media/ProductImages/")
    Price=models.IntegerField(default=0)
    Short_Discreption=models.TextField()
    Discreption=models.TextField()
    Date=models.DateField(default=datetime.today())
    def __str__(self):
        return self.Product_Name