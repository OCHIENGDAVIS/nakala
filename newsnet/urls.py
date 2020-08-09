
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('citizen/', include('citizen.urls', namespace='citizen')),
]
