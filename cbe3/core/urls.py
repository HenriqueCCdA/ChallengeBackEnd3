from cbe3.core.views import import_csv
from django.urls import path


urlpatterns = [
    path('import/', import_csv, name='import_csv'),
]
