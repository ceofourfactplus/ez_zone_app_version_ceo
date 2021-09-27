from django.urls import path
from product import views

urlpatterns = [
    path('category/', views.ProductCategoryList.as_view()),
    path('category/<int:id>/', views.ProductCategoryDetail.as_view()),
    path('sale-channel/', views.SalechannelList.as_view()),
    path('sale-channel/<int:id>/', views.SaleChannelDetail.as_view()),
    path('topping/', views.ToppingList.as_view()),
    path('topping/<int:id>/', views.ToppingDetail.as_view()),
    path('type-topping/', views.TypeToppingList.as_view()),
    path('type-topping/<int:id>/', views.TypeToppingDetail.as_view()),
    path('price-product/', views.PriceProductList.as_view()),
    path('price-product/<int:id>/', views.PriceProductDetail.as_view()),
    path('table-topping/', views.TableToppingList.as_view()),
    path('table-topping/<int:id>/', views.TableToppingDetail.as_view()),
    path('price-product/', views.PriceProductList.as_view()),
    path('price-product/<int:id>/', views.PriceProductDetail.as_view()),
    path('product/', views.ProductList.as_view()),
    path('product/<int:id>/', views.ProductDetail.as_view()),
]