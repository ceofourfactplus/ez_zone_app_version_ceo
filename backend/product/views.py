from product.models import ProductCategory,SaleChannel,Topping,TypeTopping,PriceTopping,TableTopping,PriceProduct,Product
from product.serializers import ProductCategorySerializer,SaleChannelSerializer,ToppingSerializer,TypeToppingSerializer,PriceToppingSerializer,TableToppingSerializer,PriceProductSerializer,ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ProductCategoryList(APIView):
    def get(self, request):
        category = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(category, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ProductCategoryDetail(APIView):
    def get_object(self, pk):
        try:
            return ProductCategory.objects.get(pk=pk)
        except ProductCategory.DoesNotExist:
            raise 404

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = ProductCategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = self.get_object(pk)
        serializer = ProductCategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()
        return Response(status=204)

class SalechannelList(APIView):
    def get(self, request):
        sale_channel = SaleChannel.objects.all()
        serializer = SaleChannelSerializer(sale_channel, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SaleChannelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class SaleChannelDetail(APIView):
    def get_object(self, pk):
        try:
            return SaleChannel.objects.get(pk=pk)
        except SaleChannel.DoesNotExist:
            raise 404

    def get(self, request, pk):
        sale_channel = self.get_object(pk)
        serializer = SaleChannelSerializer(sale_channel)
        return Response(serializer.data)

    def put(self, request, pk):
        sale_channel = self.get_object(pk)
        serializer = SaleChannelSerializer(sale_channel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        sale_channel = self.get_object(pk)
        sale_channel.delete()
        return Response(status=204)

class ToppingList(APIView):
    def get(self, request):
        object = Topping.objects.all()
        serializer = ToppingSerializer(object, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ToppingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ToppingDetail(APIView):
    def get_object(self, pk):
        try:
            return Topping.objects.get(pk=pk)
        except Topping.DoesNotExist:
            raise 404

    def get(self, request, pk):
        object = self.get_object(pk)
        serializer = ToppingSerializer(object)
        return Response(serializer.data)

    def put(self, request, pk):
        object = self.get_object(pk)
        serializer = ToppingSerializer(object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        object = self.get_object(pk)
        object.delete()
        return Response(status=204)

class TypeToppingList(APIView):
    def get(self, request):
        object = TypeTopping.objects.all()
        serializer = TypeToppingSerializer(object, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TypeToppingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class TypeToppingDetail(APIView):
    def get_object(self, pk):
        try:
            return TypeTopping.objects.get(pk=pk)
        except TypeTopping.DoesNotExist:
            raise 404

    def get(self, request, pk):
        object = self.get_object(pk)
        serializer = TypeToppingSerializer(object)
        return Response(serializer.data)

    def put(self, request, pk):
        object = self.get_object(pk)
        serializer = TypeToppingSerializer(object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        object = self.get_object(pk)
        object.delete()
        return Response(status=204)

class PriceToppingList(APIView):
    def get(self, request):
        object = PriceTopping.objects.all()
        serializer = PriceToppingSerializer(object, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PriceToppingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class PriceToppingDetail(APIView):
    def get_object(self, pk):
        try:
            return PriceTopping.objects.get(pk=pk)
        except PriceTopping.DoesNotExist:
            raise 404

    def get(self, request, pk):
        object = self.get_object(pk)
        serializer = PriceToppingSerializer(object)
        return Response(serializer.data)

    def put(self, request, pk):
        object = self.get_object(pk)
        serializer = PriceToppingSerializer(object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        object = self.get_object(pk)
        object.delete()
        return Response(status=204)

class TableToppingList(APIView):
    def get(self, request):
        object = TableTopping.objects.all()
        serializer = TableToppingSerializer(object, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TableToppingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class TableToppingDetail(APIView):
    def get_object(self, pk):
        try:
            return TableTopping.objects.get(pk=pk)
        except TableTopping.DoesNotExist:
            raise 404

    def get(self, request, pk):
        object = self.get_object(pk)
        serializer = TableToppingSerializer(object)
        return Response(serializer.data)

    def put(self, request, pk):
        object = self.get_object(pk)
        serializer = TableToppingSerializer(object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        object = self.get_object(pk)
        object.delete()
        return Response(status=204)

class PriceProductList(APIView):
    def get(self, request):
        object = PriceProduct.objects.all()
        serializer = PriceProductSerializer(object, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PriceProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class PriceProductDetail(APIView):
    def get_object(self, pk):
        try:
            return PriceProduct.objects.get(pk=pk)
        except PriceProduct.DoesNotExist:
            raise 404

    def get(self, request, pk):
        object = self.get_object(pk)
        serializer = PriceProductSerializer(object)
        return Response(serializer.data)

    def put(self, request, pk):
        object = self.get_object(pk)
        serializer = PriceProductSerializer(object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        object = self.get_object(pk)
        object.delete()
        return Response(status=204)

class ProductList(APIView):
    def get(self, request):
        object = Product.objects.all()
        serializer = ProductSerializer(object, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ProductDetail(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise 404

    def get(self, request, pk):
        object = self.get_object(pk)
        serializer = ProductSerializer(object)
        return Response(serializer.data)

    def put(self, request, pk):
        object = self.get_object(pk)
        serializer = ProductSerializer(object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        object = self.get_object(pk)
        object.delete()
        return Response(status=204)
