from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from . import views

app_name = 'About'
urlpatterns = [

    url(r'^$', views.HomeView.as_view(), name='basea'),
    url(r'^mission/$', views.mission),
    url(r'^team/$', views.team),
    url(r'^admin/', include(admin.site.urls)),

]
