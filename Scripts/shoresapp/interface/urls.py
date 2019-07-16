from django.urls import path
from . views import AdsListView, AdsDetailView

urlpatterns = [
    path('', AdsListView.as_view(), name='home'),
    path('ads/<slug:slug>', AdsDetailView.as_view(), name='ads-detail'),

]
