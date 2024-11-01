"""
URL configuration for Hack_UNT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# project/urls.py

from django.contrib import admin
from django.urls import path, include
from call_processor import views

# project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('incoming-call/', views.incoming_call, name='incoming_call'),
    path('recording-callback/', views.recording_callback, name='recording_callback'),
    path('admin/', admin.site.urls),
    path('audio/', include('audio_processing.urls')),  # Ensure this line is correct
]