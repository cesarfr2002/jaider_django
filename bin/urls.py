from django.urls import path
from .views import *

urlpatterns = [
    path('', bin, name='bin'),
    path('restaurar/cliente/<id>', restore_client, name='restore_client'),
    path('restaurar/proveedor/<id>', restore_provider, name='restore_provider'),
    path('eliminar/cliente/<id>', delete_client, name='delete_client'),
    path('eliminar/proveedor/<id>', delete_provider, name='delete_provider'),
]