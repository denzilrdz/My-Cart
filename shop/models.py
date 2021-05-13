from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=300, default="")
    pub_date = models.DateField()
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to="shop/images", default="") 

    def __str__(self):
        return self.product_name
    