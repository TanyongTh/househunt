from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^househunt/housescraping$', views.housescraping, name='housescraping'),
    url(r'^househunt/property_search$', views.property_search, name='property_search'),
]
    # url(r'^$', views.housescraping, name='housescraping'),
    # url(r'^$', views.property_search, name='property_search'),