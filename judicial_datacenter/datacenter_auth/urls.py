from django.conf.urls import url
from datacenter_auth.views import UserControl

urlpatterns = [
    url(r'^usercontrol/(?P<op>\w+)$',UserControl.as_view()),
    ]

