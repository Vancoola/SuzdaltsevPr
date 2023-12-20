from django.contrib import admin
from django.urls import path
from main.views import index, buy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('item/<int:pk>/', index),
    path('buy/<int:pk>/', buy)
]
