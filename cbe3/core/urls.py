from cbe3.core.views import import_csv, register, users_list
from django.urls import path


urlpatterns = [
    path('', import_csv, name='import_csv'),
    path('cadastro', register, name='register'),
    path('lista_usuarios', users_list, name='users_list'),
]
