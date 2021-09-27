from django.db import models

class ProductCategory(models.Model):
    ABLE = '1'
    DISABLE = '0'
    STATUS = (
        (ABLE,'true'),
        (DISABLE,'false')
    )
    status = models.IntegerField(choices=STATUS,default=ABLE)
    category = models.CharField(max_length=100)
    
class SaleChannel(models.Model):
    ABLE = '1'
    DISABLE = '0'
    STATUS = (
        (ABLE,'able'),
        (DISABLE,'disable')
    )
    status = models.IntegerField(choices=STATUS,default=ABLE)
    sale_channel = models.CharField(max_length=100)

class Topping(models.Model):
    ABLE = '1'
    DISABLE = '0'
    STATUS = (
        (ABLE,'able'),
        (DISABLE,'disable')
    )
    status = models.IntegerField(choices=STATUS,default=ABLE)
    name = models.CharField(max_length=50)

class TypeTopping(models.Model):
    type_topping = models.CharField(max_length=100)

class PriceTopping(models.Model):
    topping = models.ForeignKey(Topping,on_delete=models.CASCADE)
    sale_channel = models.ForeignKey(SaleChannel,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)

class TableTopping(models.Model):
    topping = models.ForeignKey(Topping,on_delete=models.CASCADE)
    sale_channel = models.ForeignKey(SaleChannel,on_delete=models.CASCADE)

class Product(models.Model):
    ABLE = '1'
    DISABLE = '0'
    STATUS = (
        (ABLE,'able'),
        (DISABLE,'disable')
    )
    status = models.IntegerField(choices=STATUS,default=ABLE)
    number = models.IntegerField(),
    name = models.CharField(max_length=100)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    type_topping = models.ForeignKey(TypeTopping,on_delete=models.PROTECT)

class PriceProduct(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    sale_channel = models.ForeignKey(SaleChannel,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)

