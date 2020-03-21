from django.urls import path, re_path
from django.conf.urls import url
from .views import index, view_post, view_category

app_name = 'imnebel'
urlpatterns = [
    path('category/<slug>', view_category,name='view_category'),
    path('post/<slug>', view_post,name='view_post'),
    path('', index, name='index'),
]
