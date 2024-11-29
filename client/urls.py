from django.urls import path
from .views import *

urlpatterns = [
    path('', list_clients, name='list_clients'),
    path('guardar/cliente', store_client, name='store_client'),
    path('actualizar/cliente/<id>', update_client, name='update_client'),
    path('mover/cliente/a/la/papelera/<id>', move_client_to_trash, name='move_client_to_trash'),
]
