from django.urls import include, path
from django.contrib.auth import views as auth_views
from simplemoc.accounts.views import register
from simplemoc.accounts.views import dashboard

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('entrar/',auth_views.LoginView.as_view(),name='login'),
    path('sair/',auth_views.LogoutView.as_view(),name='logout'),
    path('cadastre-se/', register, name='register'),
]
