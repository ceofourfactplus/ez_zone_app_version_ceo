from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)


class Supplier(models.Model):
    com_name = models.CharField(max_length=255)  # company_name
    contact = models.CharField(max_length=100)
    phone = models.IntegerField()
    address = models.CharField(max_length=500)
    descriptions = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(blank=True, null=True)
    create_by = models.ForeignKey(
        'user.User', on_delete=models.PROTECT, related_name="supplier_create_by")
    update_by = models.ForeignKey('user.User', on_delete=models.PROTECT,
                                  related_name="supplier_update_by", blank=True, null=True)


class Unit(models.Model):
    unit = models.CharField(max_length=30)


class Stock(models.Model):
    code = models.CharField(max_length=10)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    status = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    balance = models.IntegerField()
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)
    minstock = models.IntegerField()
    avg_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    min_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    max_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    max_price_supplier = models.ForeignKey(
        Supplier, on_delete=models.PROTECT, null=True, related_name="stock_max_price_supplier")
    min_price_supplier = models.ForeignKey(
        Supplier, on_delete=models.PROTECT, null=True, related_name="stock_min_price_supplier")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    create_by = models.ForeignKey(
        'user.User', on_delete=models.PROTECT, related_name="stock_create_by")
    update_by = models.ForeignKey(
        'user.User', on_delete=models.PROTECT, related_name="stock_update_by")


class StockTrance(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT)
    amount = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    create_by = models.ForeignKey(
        'user.User', on_delete=models.PROTECT, related_name="stock_trance_create_by")


class Payer(models.Model):
    FEMALE = "female"
    MALE = "male"
    GENDER = (
        (FEMALE, "ผู้หญิง"),
        (MALE, "ผู้ชาย")
    )
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=6, choices=GENDER)


class Invoice(models.Model):
    CASH = "cash"
    TRANSFER = "transfer"
    PAYMENT = (
        (CASH, 'จ่ายสด'),
        (TRANSFER, 'โอน')
    )
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.IntegerField()
    payer = models.ForeignKey(Payer, on_delete=models.PROTECT)
    payment = models.CharField(max_length=8, choices=PAYMENT)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    create_by = models.ForeignKey(
        'user.User', on_delete=models.PROTECT, related_name="invoice_create_by")
    update_by = models.ForeignKey(
        'user.User', on_delete=models.PROTECT, related_name="invoice_update_by", blank=True)


class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField()
    remark = models.TextField(blank=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    create_by = models.ForeignKey(
        'user.User', on_delete=models.PROTECT, related_name="invoice_detail_create_by")
    update_by = models.ForeignKey(
        'user.User', on_delete=models.PROTECT, related_name="invoice_detail_update_by", blank=True)


class OrderToBuy(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    amount = models.IntegerField()
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    max_price = models.DecimalField(max_digits=10, decimal_places=2)
