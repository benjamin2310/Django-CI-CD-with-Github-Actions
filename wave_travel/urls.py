from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('packages.urls')),
    path('', lambda request: HttpResponseRedirect('/api/')),  # Redirect root to /api/
    path('', home, name='home')
]

