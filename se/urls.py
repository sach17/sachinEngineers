from django.conf.urls import include, url
from . import views

app_name='se' 
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail')
]
