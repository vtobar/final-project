from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from . import views

app_name = 'home'
urlpatterns = [

    url(r'^$', views.HomeView.as_view(), name='base'),
    url(r'^admin/', include(admin.site.urls)),

]
