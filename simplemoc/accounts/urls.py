from django.urls import include, path
from django.contrib.auth import views as auth_views
from simplemoc.accounts.views import register
urlpatterns = [
    path('entrar/',auth_views.LoginView.as_view(),name='login'),
    path('cadastre-se/', register, name='register'),
]
