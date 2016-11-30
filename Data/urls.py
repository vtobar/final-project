from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from . import views

app_name = 'Data'
urlpatterns = [

    url(r'^$', views.HomeView.as_view(), name='base'),
    url(r'^data1/$', views.data1),

    url(r'^display_pic_data1', views.display_pic_data1, name= "display_pic_data1"),
    url(r'^display_pic_data1/(?P<year>[0-9]+)/$', views.display_pic_data1, name= "display_pic_data1"),
    url(r'^plot_data1/$', views.plot_data1, name= "plot_data1"),
    url(r'^plot_data1/(?P<year>[0-9]+)/$', views.plot_data1, name= "plot_data1"),
    url(r'^data2/$', views.data2),
    url(r'^display_pic_data2', views.display_pic_data2, name= "display_pic_data2"),
    url(r'^display_pic_data2/(?P<year>[0-9]+)/$', views.display_pic_data2, name= "display_pic_data2"),
    url(r'^plot_data2/$', views.plot_data2, name= "plot_data2"),
    url(r'^plot_data2/(?P<year>[0-9]+)/$', views.plot_data2, name= "plot_data2"),
    url(r'^admin/', include(admin.site.urls)),

]
