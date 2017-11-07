from django.conf.urls import include, url
from . import views

app_name='se' 
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^our-profile$', views.profile, name='our-profile'),
    url(r'^our-approach$', views.approach, name='our-approach'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail') # testing purpose
]
