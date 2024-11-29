from django.shortcuts import render, redirect, get_object_or_404
from .models import Client
from django.contrib.auth.decorators import login_required

@login_required
def list_clients(request):
    # Lista los clientes que no están marcados como eliminados
    clients = Client.objects.filter(trash=False)
    return render(request, 'clients.html', {'clients': clients})

@login_required
def store_client(request):
    # Crear un nuevo cliente con los datos del formulario
    name = request.POST['name']
    card = request.POST['card']
    phone = request.POST['phone']
    date = request.POST['date']
    medical_prescription = request.POST['medical_prescription']
    valor = request.POST.get('valor')  # Captura el valor del formulario
    
    # Validar y convertir 'valor' a entero
    if valor and valor.isdigit():
        valor = int(valor)
    else:
        valor = 0  # Valor predeterminado si no se proporciona o no es válido
    
    # Crear y guardar el nuevo cliente
    new_client = Client(
        name=name,
        card=card,
        phone=phone,
        date=date,
        medical_prescription=medical_prescription,
        valor=valor
    )
    new_client.save()
    return redirect('list_clients')

@login_required
def update_client(request, id):
    # Actualizar un cliente existente
    client = get_object_or_404(Client, pk=id)
    client.name = request.POST['name']
    client.card = request.POST['card']
    client.phone = request.POST['phone']
    client.date = request.POST['date']
    client.medical_prescription = request.POST['medical_prescription']
    valor = request.POST.get('valor')  # Captura el valor actualizado

    # Validar y convertir 'valor' a entero
    if valor and valor.isdigit():
        client.valor = int(valor)  # Actualizar solo si se proporciona un nuevo valor válido
    
    client.save()
    return redirect('list_clients')

@login_required
def move_client_to_trash(request, id):
    # Mover un cliente a la "papelera" (campo trash = True)
    client = get_object_or_404(Client, pk=id)
    client.trash = True
    client.save()
    return redirect('list_clients')
