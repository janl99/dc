# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.views.generic import View
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.contrib import auth
from django.contrib.auth.forms import PasswordChangeForm,SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
#from django.contrib.sites.models import get_current_site
from django.utils.http import (base36_to_int,is_safe_url,urlsafe_base64_decode,urlsafe_base64_encode)
from datacenter_auth.models import DatacenterUser

import time
import datetime
import os
import json
import base64
import logging

logger = logging.getLogger(__name__)
# Create your views here.

class UserControl(View):

  def post(self, request, *args, **kwargs):
    op = self.kwargs.get('op')
    logger.info("/usercontrol/ %s",op)
    if op == 'login':
      return self.login(request)
    elif op == 'logout':
      return self.logout(request)

    raise PermissionDenied

  def get(self,request, *args, **kwargs):
    raise Http404

  def login(self,request):
    username = request.POST.get("username","")
    password = request.POST.get("password","")
    user = auth.authenticate(username=username,password=password)

    errors = []

    if user is not None:
      auth.login(request,user)
    else:
      errors.append(u"密码或者用户名不正确")

    mydict = {"errors":errors}
    return HttpResponse(json.dumps(mydict),content_type="application/json")

  def logout(self,request):
    if not request.user.is_authenticated():
      logger.error(u"[UserControl]用户未登录")
      raise PermissionDenied
    else:
      auth.logout(request)
      return HttpResponse("OK")


