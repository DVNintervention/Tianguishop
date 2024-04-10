from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from authentication.views import register
from authentication import views

urlpatterns = [
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('accounts/profile/', views.profile_view, name='profile'),
    path('create-store/', views.create_seller_and_store, name='create_seller_store'),
    path('add-product/', views.add_product, name='add_product'),
    path('', views.homepage, name='homepage'),
    path('accessibility/', views.accessibility_settings_view, name='accessibility_settings'),

]
