from django.shortcuts import render, redirect, reverse
from . models import Ads
from django.conf import settings
from django.template import loader

from django.views.generic import (
ListView,
DeleteView,
CreateView,
UpdateView,
DetailView,
)
# Create your views here.


class AdsListView(ListView):
    model = Ads
    template_name = 'interface/index.html'
    context_object_name = 'ads'

class AdsDetailView(DetailView):
    model = Ads
    template_name = 'interface/ads_detail.html'