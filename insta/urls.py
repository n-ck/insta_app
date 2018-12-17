from django.conf.urls import url

from . import views

app_name = 'insta'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/$', views.GetPostImg.as_view(), name='get_post'),
    url(r'^page/$', views.GetPage.as_view(), name='get_page'),
    url(r'^savepost/(?P<page>.+)/(?P<img>.+)/$', views.SavePost.as_view(), name="save_post")
]