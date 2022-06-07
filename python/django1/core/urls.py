from django.urls import path
from .views import *
from core import views
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('', views.index, name = 'index'),
    path('index2', views.index2, name = 'index2'),
    path('sobre',sobre, name='sobre'),
    path('carrinho',carrinho, name='carrinho'),
    path('produtos', produtos, name='produtos'),
    path('produto/<int:id>', produto, name ='produto'),
    path('index',index, name='index'),
]

handler404 = views.error404
handler500 = views.error500