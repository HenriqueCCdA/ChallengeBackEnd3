from cbe3.core.views import delete_user, import_csv, register, update_user, users_list
from django.urls import path


urlpatterns = [
    path('', import_csv, name='import_csv'),
    path('cadastro/', register, name='register'),
    path('lista_usuarios/', users_list, name='users_list'),
    path('user/delete/<int:id>', delete_user, name='delete_user'),
    path('user/update/<int:id>', update_user, name='update_user'),
]
