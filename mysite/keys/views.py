from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import Key


# Create your views here.
class KeysView(generic.ListView):
    template_name = 'keys/all_keys.html'
    context_object_name = 'door_keys'

    def get_queryset(self):
        Key.objects.all()


def active_key(request, key_id):
    is_active = Key.objects.get(id=key_id).active
    return HttpResponse(f'{is_active}')
