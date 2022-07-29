from django.urls import path
from .views import active_key
from . import views

app_name = 'keys'
urlpatterns = [
    path('', views.KeysView.as_view(), name='all_keys'),
    path('<uuid:key_id>/', active_key, name='active_key')

]
