from django.shortcuts import render,render_to_response
from django.views.generic import View,TemplateView,ListView,DetailView
from django.contrib import auth
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
import logging
# Create your views here.

#logger
logger = logging.getLogger(__name__)


class BaseMixin(object):
    def get_context_data(self, *args, **kwargs):
        context = super(BaseMixin,self).get_context_data(**kwargs)
        try:
            context['website_title'] = settings.WEBSITE_TITLE
            context['website_welcome'] = settings.WEBSITE_WELCOME

            user = self.request.user
            if user.is_authenticated():
                context['notificaton_count'] = 1
        except Exception as e:
            logger.error(u'[BaseMixin] load base info on exception')

        return context

class IndexView(BaseMixin,ListView):
    template_name = "datacenter/index.html"
    context_object_name = "model_list"

    def get_context_data(self, **kwargs):
        kwargs['carousel_page_list'] = ["page_1","page_2","page_3"]
        return super(IndexView,self).get_context_data(**kwargs)

    def get_queryset(self):
        model_list = ["model_1","model_2","model_3"] 
        return model_list


