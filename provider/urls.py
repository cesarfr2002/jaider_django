from django.urls import path
from .views import *

urlpatterns = [
    path('', list_providers, name='list_providers'),
    path('guardar/proveedor', store_provider, name='store_provider'),
    path('actualizar/proveedor/<id>', update_provider, name='update_provider'),
    path('mover/proveedor/a/la/papelera/<id>', move_provider_to_trash, name='move_provider_to_trash'),
]
