
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='ContactUs'),
    path('productView', views.productView, name='productView'),
    path('shop', include('shop.urls')) ,
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)