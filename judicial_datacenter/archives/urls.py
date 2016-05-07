from django.conf.urls import url
from . import views 

urlpatterns =[
    url(r'^jglbs/$',views.JGLBList.as_view()),
    url(r'^jglbs/(?P<pk>[0-9]+)/$',views.JGLBDetail.as_view()),
    ]
