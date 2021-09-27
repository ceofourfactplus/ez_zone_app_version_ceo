from django.urls import path
from . import views
urlpatterns = [
    path('supplier/', views.SupplierListAPIView.as_view()),
    path('unit/', views.UnitListAPIView.as_view()),
    path('stock/', views.StockListAPIView.as_view()),
    path('stock-trance/', views.StockTranceListAPIView.as_view()),
    path('payer/', views.PayerListAPIView.as_view()),
    path('invoice/', views.InvoiceListAPIView.as_view()),
    path('invoice-detail/', views.InvoiceDetailListAPIView.as_view()),
    path('order-to-buy/', views.OrderToBuyListAPIView.as_view()),
    path('supplier/<int:pk>/', views.SupplierDetailAPIView.as_view()),
    path('unit/<int:pk>/', views.UnitDetailAPIView.as_view()),
    path('stock/<int:pk>/', views.StockDetailAPIView.as_view()),
    path('stock-trance/<int:pk>/', views.StockTranceDetailAPIView.as_view()),
    path('payer/<int:pk>/', views.PayerDetailAPIView.as_view()),
    path('invoice/<int:pk>/', views.InvoiceDetailAPIView.as_view()),
    path('invoice-detail/<int:pk>/', views.InvoiceDetailDetailAPIView.as_view()),
    path('order-to-buy/<int:pk>/', views.OrderToBuyDetailAPIView.as_view()),
    path('delete-all', views.DeleteAllDataAPIView.as_view())
]
