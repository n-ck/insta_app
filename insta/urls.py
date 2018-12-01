from django.conf.urls import url

from . import views

app_name = 'insta'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/$', views.GetPostImg.as_view(), name='get_post'),
]