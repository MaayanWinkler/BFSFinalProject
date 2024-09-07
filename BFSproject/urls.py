"""BFSproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from BFSapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.user_login, name="user_login"),
    path("index", views.index, name="index"),
    path("forms/eggsMonitorForm", views.fill_eggs_monitor_form, name="fill_eggs_monitor_form"),
    path("forms/rearingMonitorForm", views.fill_rearing_monitor_form, name="fill_rearing_monitor_form"),
    path("forms/breedingMonitorForm", views.fill_breeding_monitor_form, name="fill_breeding_monitor_form"),
    path("tables/eggMonitorTable", views.get_egg_monitor_table, name="get_egg_monitor_table"),
    path("tables/rearingMonitorTable", views.get_rearing_monitor_table, name="get_rearing_monitor_table"),
    path("tables/breedingMonitorTable", views.get_breeding_monitor_table, name="get_breeding_monitor_table"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)