from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic.base import TemplateView

# from django.urls import reverse # future versions.
from django.core.urlresolvers import reverse_lazy
# Create your views here.
class HomeView(TemplateView):

    template_name = 'base.html'
