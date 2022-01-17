from django.urls import path
from . import views

urlpatterns = [
  path('register/',views.RegisterUserAPIView.as_view()),
  path('user-info/', views.UserInfo.as_view()),
  # path('activate-user/',views.activate_user,name='activate')
]