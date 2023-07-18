from django.urls import path
from .views import SignUpView,LoginView
from account import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('signin/', views.LoginView.as_view(), name="signin"),
]