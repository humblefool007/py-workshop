from django.urls import path, re_path
from blog import views

urlpatterns = [
re_path(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    re_path(r'^post/new/$', views.post_new, name='post_new'),
    re_path(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    re_path(r'^category/(?P<type>\d+)/$', views.list_category, name='list_category'),
    re_path(r'^mypost/$', views.mypost, name='mypost'),
    re_path(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
re_path(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),

]

