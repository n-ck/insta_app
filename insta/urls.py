from django.conf.urls import url

from . import views

app_name = 'insta'

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^post/$', views.GetPostImg.as_view(), name='get_post'),
    url(r'^post/(?P<postid>\d+)/$', views.PostDetail.as_view(), name="post_detail"),
    url(r'^page/$', views.GetPage.as_view(), name='get_page'),
    url(r'^savepost/(?P<page>[\w-]+)/(?P<img>.+)/$', views.SavePost.as_view(), name="save_post"),
    url(r'^savedposts/$', views.ViewSaved.as_view(), name="view_saved")
]