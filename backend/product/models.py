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
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    create_by = models.ForeignKey(
        'user.User', on_delete=models.PROTECT, related_name="product_category_create_by")
    update_by = models.ForeignKey(
        'user.User', on_delete=models.PROTECT, related_name="product_category_update_by")
    
class SaleChannel(models.Model):
    ABLE = '1'
    DISABLE = '0'
    STATUS = (
        (ABLE,'able'),
        (DISABLE,'disable')
    )
    status = models.IntegerField(choices=STATUS,default=ABLE)
    sale_channel = models.CharField(max_length=100)
    create_by = models.ForeignKey(
        'user.User', on_delete=models.PROTECT, related_name="sale_channel_create_by")
    update_by = models.ForeignKey(
        'user.User', on_delete=models.PROTECT, related_name="sale_channel_update_by")


class Topping(models.Model):
    ABLE = '1'
    DISABLE = '0'
    STATUS = (
        (ABLE,'able'),
        (DISABLE,'disable')
    )
    status = models.IntegerField(choices=STATUS,default=ABLE)
    name = models.CharField(max_length=50)
    create_by = models.ForeignKey(
        'user.User', on_delete=models.PROTECT, related_name="topping_create_by")
    update_by = models.ForeignKey(
        'user.User', on_delete=models.PROTECT, related_name="topping_update_by")


class TypeTopping(models.Model):
    type_topping = models.CharField(max_length=100)
    create_by = models.ForeignKey(
        'user.User', on_delete=models.PROTECT, related_name="type_topping_create_by")
    update_by = models.ForeignKey(
        'user.User', on_delete=models.PROTECT, related_name="type_topping_update_by")


class PriceTopping(models.Model):
    topping = models.ForeignKey(Topping,on_delete=models.CASCADE)
    sale_channel = models.ForeignKey(SaleChannel,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    create_by = models.ForeignKey(
        'user.User', on_delete=models.PROTECT, related_name="price_topping_create_by")
    update_by = models.ForeignKey(
        'user.User', on_delete=models.PROTECT, related_name="price_topping_update_by")


class TableTopping(models.Model):
    topping = models.ForeignKey(Topping,on_delete=models.CASCADE)
    sale_channel = models.ForeignKey(SaleChannel,on_delete=models.CASCADE)
    create_by = models.ForeignKey(
        'user.User', on_delete=models.PROTECT, related_name="table_topping_create_by")
    update_by = models.ForeignKey(
        'user.User', on_delete=models.PROTECT, related_name="table_topping_update_by")


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
    create_by = models.ForeignKey(
        'user.User', on_delete=models.PROTECT, related_name="product_create_by")
    update_by = models.ForeignKey(
        'user.User', on_delete=models.PROTECT, related_name="product_update_by")


class PriceProduct(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    sale_channel = models.ForeignKey(SaleChannel,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    create_by = models.ForeignKey(
        'user.User', on_delete=models.PROTECT, related_name="price_product_create_by")
    update_by = models.ForeignKey(
        'user.User', on_delete=models.PROTECT, related_name="price_product_update_by")


