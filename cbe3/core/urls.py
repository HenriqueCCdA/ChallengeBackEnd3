from cbe3.core.views import home
from django.urls import path


urlpatterns = [
    path('', home, name='home'),
]
