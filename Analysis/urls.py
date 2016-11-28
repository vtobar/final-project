from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from . import views

app_name = 'Analysis'
urlpatterns = [

    url(r'^$', views.HomeView.as_view(), name='analysis'),
    url(r'^crime/$', views.crime),
    url(r'^crime_reg/$', views.crime_reg),
    url(r'^admin/', include(admin.site.urls)),

]
