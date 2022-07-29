from django.urls import path
from .views import check_key
from . import views

app_name = 'keys'
urlpatterns = [
    path('', views.KeysView.as_view(), name='all_keys'),
    path('check/<uuid:key_id>/', check_key, name='check_key')

]
