from django.contrib import admin
from .models import Key


class KeyAdmin(admin.ModelAdmin):
    list_display = ('card_id', 'active')


# Register your models here.
admin.site.register(Key, KeyAdmin)
