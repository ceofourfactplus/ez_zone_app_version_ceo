
from django.db import models
from product.models import SaleChannel, Product, Topping

class Order(models.Model):
    DELIVERY = '1'
    EATHERE = '0'
    STATUS_DELIVERY = (
        (DELIVERY,'delivery'),
        (EATHERE,'eat_here')
    )
    
    ON_COOKING = '1'
    ON_DELIVERY = '2'
    FINISH = '3'
    STATUS_ORDER = (
        (ON_COOKING,'cooking'),
        (ON_DELIVERY,'delivery'),
        (FINISH,'finish'),
    )

    status_delivery = models.IntegerField(choices=STATUS_DELIVERY)
    total_price = models.DecimalField(max_digits=10,decimal_places=2)
    total_amount = models.IntegerField()
    sale_channel = models.ForeignKey(SaleChannel,on_delete=models.PROTECT)
    customer_name = models.CharField(max_length=100)
    descriptions = models.TextField()
    status_order = models.IntegerField(choices=STATUS_ORDER,default=ON_COOKING)
    create_by = models.ForeignKey(
        'user.User', on_delete=models.PROTECT, related_name="order_create_by")
    update_by = models.ForeignKey(
        'user.User', on_delete=models.PROTECT, related_name="order_update_by")


class OrderItem(models.Model):
    FLAVOUR_0 = '0'
    FLAVOUR_50 = '1'
    FLAVOUR_100 = '2'
    FLAVOUR_150 = '3'
    FLAVOUR_LEVEL = (
        (FLAVOUR_0,'non'),
        (FLAVOUR_50,'low'),
        (FLAVOUR_100,'midium'),
        (FLAVOUR_150,'much')
    )

    SPICY = "1"
    SWEET = "2"
    FLAVOUR_TYPE = (
        (SPICY,'spicy'),
        (SWEET,'sweet')
    )

    flavour_level = models.IntegerField(choices=FLAVOUR_LEVEL)
    flavour_type = models.IntegerField(choices=FLAVOUR_TYPE)
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10,decimal_places=2)
    desscriptions = models.TextField()
    amount = models.IntegerField()

class OrderItemTopping(models.Model):
    item = models.ForeignKey(OrderItem,on_delete=models.CASCADE)
    topping = models.ForeignKey(Topping,on_delete=models.PROTECT)
    total_price = models.DecimalField(max_digits=10 ,decimal_places=2)
    amount = models.IntegerField()
