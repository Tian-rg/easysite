from django.conf.urls import url
from . import views  

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^notes$', views.notes, name="notes"),
    url(r'^calculator/(?P<year>[0-9]{4})/$', 
    views.year_archive, name="year_achive"),
]