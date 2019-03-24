from django.urls import path

from basic_app.views import blog_listing
from .views import (
   blog_details,
    # post_model_create_view,
    # post_model_detail_view,
    # post_model_delete_view,
    # post_model_list_view,
    # post_model_update_view
    )

urlpatterns = [
    path('', blog_listing,name='blog'),
    path('<slug:slug>', blog_details, name='detail'),
    # path('hapus/<int:list_gallery_id>', hapus_foto, name='hapus_foto'),

    # path(r'^$', post_model_list_view, name='list'),
    # path(r'^create/$', post_model_create_view, name='create'),
    # path(r'^(?P<id>\d+)/delete/$', post_model_delete_view, name='delete'),
    # path(r'^(?P<id>\d+)/edit/$', post_model_update_view, name='update'),
    #path(r'^admin/', admin.site.paths),
    #path(r'^$', home, name='home'),
    #path(r'^redirect/$', redirect_somewhere, name='home')
]
