from django.db import models



class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="aaa")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)  
    image  = models.ImageField(upload_to="shop/images",default="aaa")
    
    
    def __str__(self):
        return self.product_name    #returns respective product name