"""
URL configuration for first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path,include  # Import include to include other URL configurations
from first_app import views
from django.conf import settings
from django.conf.urls.static import static
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),  # Add this line for the index view
    path('',include('first_app.urls')),  # Add this line for the first_app view
    path('admin/', admin.site.urls),
    path('formpage/', views.form_name_view, name='form_name'),  # Add this line for the form view
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

