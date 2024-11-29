from django.shortcuts import render, redirect, get_object_or_404
from .models import Provider
from django.contrib.auth.decorators import login_required
from django.http import Http404

@login_required
def list_providers(request):
    providers = Provider.objects.filter(trash=False)
    return render(request, 'providers.html', {'providers': providers})

@login_required
def store_provider(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        product = request.POST.get('product')
        valor = request.POST.get('valor')

        # Validación de campos vacíos
        if not name or not product or not valor:
            return render(request, 'providers.html', {'error': 'Todos los campos son obligatorios'})
        
        # Crear nuevo proveedor
        new_provider = Provider(name=name, product=product, valor=valor)
        new_provider.save()
        return redirect('list_providers')

    return render(request, 'providers.html')

@login_required
def update_provider(request, id):
    provider = get_object_or_404(Provider, pk=id)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        product = request.POST.get('product')
        valor = request.POST.get('valor')

        # Validación de campos vacíos
        if not name or not product or not valor:
            return render(request, 'update_provider.html', {'error': 'Todos los campos son obligatorios', 'provider': provider})

        # Actualizar proveedor
        provider.name = name
        provider.product = product
        provider.valor = valor
        provider.save()
        return redirect('list_providers')

    return render(request, 'update_provider.html', {'provider': provider})

@login_required
def move_provider_to_trash(request, id):
    try:
        provider = Provider.objects.get(pk=id)
        provider.trash = True
        provider.save()
    except Provider.DoesNotExist:
        raise Http404("Proveedor no encontrado")
    
    return redirect('list_providers')
