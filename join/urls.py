from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('deleta/<int:pk>', views.deleta_coordedana, name='deleta'),
    path('atualiza/<int:pk>', views.atualiza_coordedana, name='atualiza')
]
