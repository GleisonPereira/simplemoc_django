from django.urls import path
from simplemoc.courses.views import index
from simplemoc.courses.views import details

urlpatterns = [
    path('', index, name='index'),
    #path('<int:pk>/', details, name='details'),
    path('<slug:slug>/', details, name='details'),
]
