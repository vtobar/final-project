from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse # future versions.
from django.core.urlresolvers import reverse_lazy
from os.path import join
from django.conf import settings
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
from .forms import YearsForm
#from .models import STATES_DICT, CURRENCY_DICT

from django.views.generic.base import TemplateView
import seaborn as sns
from io import BytesIO

class HomeView(TemplateView):

    template_name = 'baseny.html'

from os.path import join
from django.conf import settings
from django.views.generic import FormView
from .forms import YearsForm


def csv(request, year = None):
   filename = join(settings.STATIC_ROOT, 'Data/MASTER1.csv')
   df = pd.read_csv(filename)
   if year: df = df[df["Year"] == int(year)]
   table = df.to_html(float_format = "%.3f", classes = "table table-striped", index_names = False)
   table = table.replace('border="1"','border="0"')
   table = table.replace('style="text-align: right;"', "") # control this in css, not pandas.
   return HttpResponse(table)

class FormClass(FormView):

    template_name= 'data1.html'
    form_class = YearsForm

from .forms import YearsForm
from django.core.urlresolvers import reverse_lazy

from .forms import YearsForm
def display_pic_data1(request):

    year = int(request.GET.get('year', 2005))

    params = { 'title': year,
              'form_action' : reverse_lazy('Data:data1'),
              'form_method' : 'get',
              'form': YearsForm({'year': year}),
              'pic_source' : reverse_lazy("Data:plot_data1", kwargs = { 'c' : year})
              }

    return render(request, 'view_pic.html', params)

def plot_data1(request, c = 2011):

    filename = join(settings.STATIC_ROOT, 'Data/MASTER1.csv')

    suicide = pd.read_csv(filename)

    suicide = suicide[suicide['Year'] == c]
    if not suicide.size: return HttpResponse("No such year!")

    suicide['% Deaths by Suicide'] = suicide['Percentage Deaths by Suicide']*100

    suicide_graph = suicide.sort_values(by = "% Deaths by Suicide", ascending = False).head(10)


    sns.set(style="ticks")
    flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]

    x = suicide_graph["County"]
    y = suicide_graph["% Deaths by Suicide"]


    g = sns.barplot(x, y, palette=sns.color_palette(flatui))

    # remove the top and right line in graph
    sns.despine()

    # Set the size of the graph from here
    g.figure.set_size_inches(12,7)
    # Set the Title of the graph from here
    g.axes.set_title('Percentage Deaths by Suicide',
        fontsize=34,color="b",alpha=0.3)
    # Set the xlabel of the graph from here
    g.set_xlabel("County",size = 26,color="b",alpha=0.5)
    # Set the ylabel of the graph from here
    g.set_ylabel("Percentage Death by Suicides",size = 26,color="b",alpha=0.5)
    # Set the ticklabel size and color of the graph from here
    g.tick_params(labelsize=14,labelcolor="black")

      # write bytes instead of file.
    figfile = BytesIO()

    # this is where the color is used.

    try: g.figure.savefig(figfile, format = 'png')
    except ValueError: raise Http404("No such color")

    figfile.seek(0) # rewind to beginning of file
    return HttpResponse(figfile.read(), content_type="image/png")




from .forms import YearsForm
from django.core.urlresolvers import reverse_lazy
def data1(request, c = 'r'):


    filename = join(settings.STATIC_ROOT, 'Data/MASTER1.csv')

    suicide = pd.read_csv(filename)

    year = int(request.GET.get('year', 2003))
    suicide = suicide[suicide['Year'] == year]

    suicide['% Deaths by Suicide'] = suicide['Percentage Deaths by Suicide']*100
    table = suicide[['Year', 'County', 'Average NY AGI', 'Crime_Total', '% Deaths by Suicide']]

    if not table.size: return HttpResponse('No such year')

    table1 = table.to_html(float_format = "%.3f", classes = "table table-striped", index = False)
    table1 = table1.replace('border="1"','border="0"')
    table1 = table1.replace('style="text-align: right;"', "") # control this in css, not pandas.


    params = { 'title' : year,
               'form_action' : reverse_lazy('Data:data1'),
               'form_method' : 'get',
               'form': YearsForm({'year': year}),
               'html_table': table1,
               'pic_source' : reverse_lazy(("Data:plot_data1"),kwargs = { 'c' : year})
               }

    return render(request, 'data1.html', params)


def data2(request):

    filename = join(settings.STATIC_ROOT, 'Data/SUICIDE.csv')


    age_group = pd.read_csv(filename)


    year = int(request.GET.get('year', 2003))
    age_group = age_group[age_group['Year'] == year]

    pretable = age_group[age_group['Category'] == 'Age_Group']
    tablec = pretable[pretable['Category Value'] != 'Total']

    if not tablec.size: return HttpResponse('No such year')

    table2 = tablec.to_html(float_format = "%.3f", classes = "table table-striped", index = False)
    table2 = table2.replace('border="1"','border="0"')
    table2 = table2.replace('style="text-align: right;"', "") # control this in css, not pandas.

    params = {
               'form_method' : 'get',
               'form': YearsForm({'year': year}),
               'html_table': table2}


    return render(request, 'data2.html', params)






# Create your views here.
