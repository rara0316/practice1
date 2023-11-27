from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('', views.main, name='main'), #메인화면
  path('login/',auth_views.LoginView.as_view(), name='login'), #로그인화면
  path('register/', views.register, name='register'), #회원가입페이지
]
