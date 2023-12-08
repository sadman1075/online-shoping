from django.db import models

# Create your models here.
class sadman(models.Model):
    username=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    thana=models.CharField(max_length=100)
    area=models.CharField(max_length=100)
    images=models.FileField(null=True,blank=True,upload_to="images/")


class product2(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    subcategory=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    dese=models.CharField(max_length=300)
    pub_data=models.DateField()
    image=models.ImageField(upload_to='images/')

    def __str__(self) :
        return self.product_name
    
class orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    phone_no=models.CharField(max_length=1500)
    address=models.CharField(max_length=150)
    city=models.CharField(max_length=150)
    state=models.CharField(max_length=150)




