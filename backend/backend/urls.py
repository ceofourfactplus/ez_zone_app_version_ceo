from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('product.urls')),
    path('pos/', include('pos.urls')),
    path('stock/', include('stock.urls')),
    path('api-token/', TokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),
    path('user/me/', views.UserInfo.as_view()),
    path('auth/', include('user.urls'))
]
