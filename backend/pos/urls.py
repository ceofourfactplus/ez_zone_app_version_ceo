from django.urls import path
from pos import views

  
urlpatterns = [
    path('order/', views.OrderList.as_view()),
    path('order/<int:id>/', views.OrderDetail.as_view()),
    path('order-item/', views.OrderItemList.as_view()),
    path('order-item/<int:id>/', views.OrderItemDetail.as_view()),
    path('order-item-topping/', views.OrderItemToppingList.as_view()),
    path('order-item-topping/<int:id>/', views.OrderItemToppingDetail.as_view()),
]
