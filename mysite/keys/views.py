from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Key


# Create your views here.
class KeysView(generic.ListView):
    template_name = 'keys/all_keys.html'
    context_object_name = 'all_keys'

    def get_queryset(self):
        return Key.objects.all()


def check_key(request, key_id):
    # is_active = Key.objects.get(id=key_id).active
    is_active = get_object_or_404(Key, id=key_id).active
    return HttpResponse(f'{is_active}')
