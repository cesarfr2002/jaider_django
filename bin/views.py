from django.shortcuts import render, redirect
from client.models import Client
from provider.models import Provider
from django.contrib.auth.decorators import login_required

@login_required
def bin(request):
    clients = Client.objects.filter(trash=True)
    providers = Provider.objects.filter(trash=True)
    return render(request, 'bin.html', {'clients':clients, 'providers':providers})

@login_required
def restore_client(request, id):
    client = Client.objects.get(pk=id)
    client.trash = False
    client.save()
    return redirect('bin')

@login_required
def restore_provider(request, id):
    provider = Provider.objects.get(pk=id)
    provider.trash = False
    provider.save()
    return redirect('bin')

@login_required
def delete_client(request, id):
    client = Client.objects.get(pk=id)
    client.delete()
    return redirect('bin')

@login_required
def delete_provider(request, id):
    provider = Provider.objects.get(pk=id)
    provider.delete()
    return redirect('bin')

