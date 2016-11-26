from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from . import views

app_name = 'prevention'
urlpatterns = [

    url(r'^$', views.HomeView.as_view(), name='prevention'),
    url(r'^risk/$', views.risk),
    url(r'^support/$', views.support),
    url(r'^admin/', include(admin.site.urls)),


]
