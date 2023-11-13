from typing import Any
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from stats.models import (Statistic, DataItem)


class StatisticListView(generic.ListView):
    model = Statistic
    template_name = 'stats/main.html'
    queryset = Statistic.objects.all()
    context_object_name = 'statistics'    


class StatisticCreateView(generic.CreateView):
    model = Statistic
    fields = ['name']
    success_url = reverse_lazy('stats:statistics')
    template_name = 'stats/main.html'
    

class Dashboard(generic.DetailView):
    template_name = 'stats/dashboard.html'
    model = Statistic
    context_object_name = 'statistic'

