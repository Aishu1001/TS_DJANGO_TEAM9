"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add an URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from hello.views import myfunction

 
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
 
urlpatterns = (
    url(r'hello/$',myfunction),
    # Examples:
    # url(r'^$', 'sample.views.home', name='home'),
    # url(r'^sample/', include('sample.foo.urls')),
 
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
 
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
   
)
