from django.conf.urls import url

from datacenter.views import (IndexView)
from django.views.generic import TemplateView,DetailView

urlpatterns = [

    url(r'^$',IndexView.as_view(),name='index-view'),

    ]
