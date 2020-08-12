from django.urls import path
from .views import index, detail

app_name = 'citizen'

urlpatterns = [
    path('', index,  name='index'),
    path('<id>', detail,  name='detail'),
]
