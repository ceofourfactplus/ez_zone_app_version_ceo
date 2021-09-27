from rest_framework import serializers
from .models import Category, Payer, Stock, Invoice, OrderToBuy, Supplier, Unit, StockTrance, InvoiceDetail


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        modal = Category
        fields = 'all'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


class StockSerializer(serializers.ModelSerializer):
    unit_id = serializers.IntegerField()
    unit_set = UnitSerializer(read_only=True, source="unit")
    category_id = serializers.IntegerField()
    category_set = CategorySerializer(read_only=True, source="category")

    class Meta:
        model = Stock
        fields = ['id', 'code', 'status', 'name', 'balance', 'unit_id', 'minstock', 'avg_price', 'max_price', 'min_price', 'create_by', 'update_by',
                  'create_at', 'update_at', 'unit_set', 'category_id', 'category_set']


class StockTranceSerializer(serializers.ModelSerializer):
    stock_set = StockSerializer(read_only=True, source="stock")
    stock_id = serializers.IntegerField()

    class Meta:
        model = StockTrance
        fields = ['id', 'stock_set', 'stock_id',
                  'amount', 'create_at', 'create_by']


class PayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payer
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    payer_set = PayerSerializer(read_only=True, source="payer")
    supplier_set = SupplierSerializer(read_only=True, source="supplier")
    supplier_id = serializers.IntegerField()
    payer_id = serializers.IntegerField()
    create_by_id = serializers.IntegerField()
    update_by_id = serializers.IntegerField()

    class Meta:
        model = Invoice
        fields = ['id', 'supplier_id', 'total_price', 'total_amount', 'payer_id', 'payment',
                  'create_at', 'create_by_id', 'update_by_id', 'update_at', 'supplier_set', 'payer_set']


class InvoiceDetailSerializer(serializers.ModelSerializer):
    invoice_id = serializers.IntegerField()
    stock_id = serializers.IntegerField()
    invoice_set = InvoiceSerializer(read_only=True, source="invoice")
    stock_set = StockSerializer(read_only=True, source="stock")
    create_by_id = serializers.IntegerField()
    update_by_id = serializers.IntegerField()
    supplier_id = serializers.IntegerField()
    supplier_set = SupplierSerializer(read_only=True, source="supplier")

    class Meta:
        model = InvoiceDetail
        fields = ['id', 'invoice_id', 'stock_id', 'price', 'total_price', 'amount', 'remark', 'discount', 'create_at',
                  'create_by_id', 'update_at', 'update_by_id', 'supplier_id', 'supplier_set', 'invoice_set', 'stock_set']


class OrderToBuySerializer(serializers.ModelSerializer):
    stock_id = serializers.IntegerField()
    stock_set = StockSerializer(read_only=True, source="stock")
    invoice_id = serializers.IntegerField()
    invoice_set = InvoiceSerializer(read_only=True, source="inovice")

    class Meta:
        model = OrderToBuy
        fields = ['id', 'stock_id', 'stock_set', 'invoice_id',
                  'invoice_set', 'amount', 'min_price', 'max_price']
