from django.db.models import fields
from rest_framework import serializers
from rest_framework.exceptions import server_error
from product.models import ProductCategory, SaleChannel, Topping, TypeTopping, PriceTopping, TableTopping, Product, PriceProduct

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id','category']

class SaleChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleChannel
        fields = ['id','sale_channel']

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ['id','status','name']

class TypeToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeTopping
        fields = ['id','type_topping']

class PriceToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceTopping
        fields = ['id','topping','sale_channel','price']
    
class TableToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableTopping
        fields = ['id','topping','sale_channel']

class PriceProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceProduct
        fields = ['id','product','sale_channel','price']

class ProductSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Product
        fields = ['id','status','number','category','type_topping']
