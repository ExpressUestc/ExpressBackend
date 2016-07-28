from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pic/$',views.pic,name='pic'),
    url(r'^sending/$',views.sending,name='sending'),
    url(r'^find/$',views.find,name='find'),
    url(r'^distribute/$',views.distribute,name='distribute'),
    url(r'^auth/$',views.auth,name='auth'),
    url(r'^authPost/$',views.authPost,name='authPost'),
    url(r'^getVerify/$',views.getVerify,name='getVerify'),
    url(r'^authVerify/$',views.authVerify,name='authVerify'),
    url(r'^test/$',views.test,name='test'),
    url(r'^authDeliver/$',views.authDeliver,name='authDeliver'),
    url(r'^employee/$',views.employee,name='employee')
]
