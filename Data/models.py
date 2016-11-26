from django.db import models

# Create your models here.

YEARS = (
    ("2003", "2003"),
    ("2004", "2004"),
    ("2005", "2005"),
    ("2006", "2006"),
    ("2007", "2007"),
    ("2008", "2008"),
    ("2009", "2009"),
    ("2010", "2010"),
    ("2011", "2011"),
    ("2012", "2012"),
    ("2013", "2013"),
    )





class Years(models.Model):
    year = models.CharField(choices=YEARS, max_length=10)
