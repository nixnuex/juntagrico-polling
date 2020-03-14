"""
test URL Configuration for juntagrico_polling development
"""
from django.conf.urls import include, url
from django.contrib import admin
import juntagrico

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('juntagrico.urls')),
    path('', include('juntagrico_polling.urls')),
    url(r'^$', juntagrico.views.home),
]
