from django.shortcuts import render
import datetime
from time import gmtime, strftime



def index(request):
   return render(request, "index.html")

def current_date(request):
   date = strftime("%Y-%m-%d %H:%M:%S", gmtime())
   return render(request, 'index_date.html', locals())

def math_operation(request):
   x = 99 + 32 - 17 / 55
   return render(request, 'index_date.html', locals())

