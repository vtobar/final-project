from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse # future versions.
from django.core.urlresolvers import reverse_lazy
from os.path import join
from django.conf import settings
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
from django.views.generic.base import TemplateView
import seaborn as sns
from io import BytesIO

class HomeView(TemplateView):

    template_name = 'analysis.html'


from scipy import stats
import statsmodels.formula.api as sm

def crime_reg(request):

    filename = join(settings.STATIC_ROOT, 'Analysis/MASTER1.csv')

    suicide = pd.read_csv(filename)

    plt.figure()

    suicide['% Deaths by Suicide'] = suicide['Percentage Deaths by Suicide']*100
    suicide['log_income'] = np.log(suicide['Average NY AGI'])
    suicide["Crime_1000"]= np.log(suicide['Crime_Total'])
    reg = sns.regplot(data = suicide, x = "Crime_1000", y = "% Deaths by Suicide")

     # write bytes instead of file.
    figfile = BytesIO()

    # this is where the color is used.

    try: reg.figure.savefig(figfile, format = 'png')
    except ValueError: raise Http404("No such color")

    figfile.seek(0) # rewind to beginning of file

    return HttpResponse(figfile.read(), content_type="image/png")


def crime(request):

    return render(request, 'crime.html')
