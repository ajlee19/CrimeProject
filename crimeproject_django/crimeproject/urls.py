"""crimeproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^stayfe.html$', views.main, name='main'),
    url(r'^aboutus.html$', views.intro, name='intro'),
    url(r'^map.html$', views.content, name='content'),
    url(r'^contacts.html$', views.contact, name='contact'),
    # url(r'^_map.html$', views.map, name='map'),
    # url(r'^visualizemap/', include('visualizemap.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
