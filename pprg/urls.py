from django.urls import path
from .views import (
   dashboard,
   tambah_kostumer,
   tambah_peg_swasta,
   tambah_wiraswasta,
   edit_kostumer_pns,
   data_kavling,
   tambah_kavling,
   list_marketer,
   tambah_marketer,
   kegiatan_marketing,
   laporan_marketing,
   edit_kavling,
   flpp_print,
   sphj_print,
   list_swasta,
   list_wiraswasta,
   laporan,
   progress,
   progress2,
   edit_kostumer_wiraswasta,
   edit_kostumer_swasta,
   rekap_akad,
   hapus_kostumer,
   hapus_kavling,
   hapus_marketer,

    # post_model_create_view,
    # post_model_detail_view,
    # post_model_delete_view,
    # post_model_list_view,
    # post_model_update_view
    )

urlpatterns = [
    path('', dashboard,name='pprg'),
    path('list_swasta/', list_swasta,name='list swasta'),
    path('list_wiraswasta/', list_wiraswasta,name='list wiraswasta'),

    # path('tambah/', tambah_kostumer,name='tambah'),
    path('edit/<slug:slug>', edit_kostumer_pns),
    path('edit_wiraswasta/<slug:slug>', edit_kostumer_wiraswasta),
    path('edit_swasta/<slug:slug>', edit_kostumer_swasta),


    path('tambah_pns', tambah_kostumer,name='tambah_pns'),
    path('tambah_pegawai_swasta/', tambah_peg_swasta,name='tambah_pegawai_swasta'),
    path('tambah_wiraswasta/', tambah_wiraswasta,name='tambah_wiraswasta'),
    path('flpp_print/<slug:slug>', flpp_print,name='flpp'),
    path('list_swasta/flpp_print/<slug:slug>', flpp_print,name='flpp'),
    path('list_wiraswasta/flpp_print/<slug:slug>', flpp_print,name='flpp'),


    path('sphj_print/<slug:slug>', sphj_print,name='sphj'),
    path('list_swasta/sphj_print/<slug:slug>', sphj_print,name='sphj'),
    path('list_wiraswasta/sphj_print/<slug:slug>', sphj_print,name='sphj'),



    path('kavling/', data_kavling,name='kavling'),
    path('tambah_kavling/', tambah_kavling,name='tambah_kavling'),
    path('kavling/edit/<slug:slug>/', edit_kavling,name='edit_kavling'),
    path('kavling/hapus/<slug:slug>', hapus_kavling),


    path('marketer/', list_marketer,name='marketer'),
    path('marketer/hapus/<slug:slug>', hapus_marketer),
    path('tambah_marketer/', tambah_marketer,name='tambah_marketer'),
    path('kegiatan_marketing/', kegiatan_marketing,name='kegiatan_marketing'),
    path('marketer/laporan/<slug:slug>', laporan_marketing),

    path('laporan/', laporan,name='laporan'),
    path('dokumen_dan_progress/', progress,name='dokumen_dan_progress'),
    path('dokumen_dan_progress/hapus/<slug:slug>', hapus_kostumer),

    path('kpr/', progress2,name='progress_kpr'),
    path('rekap_akad/', rekap_akad,name='rekap_akad'),



    # path('', blog_listing,name='blog'),
    # path('<slug:slug>', blog_details, name='detail'),
    # path('hapus/<int:list_gallery_id>', hapus_foto, name='hapus_foto'),

    # path(r'^$', post_model_list_view, name='list'),
    # path(r'^create/$', post_model_create_view, name='create'),
    # path(r'^(?P<id>\d+)/delete/$', post_model_delete_view, name='delete'),
    # path(r'^(?P<id>\d+)/edit/$', post_model_update_view, name='update'),
    #path(r'^admin/', admin.site.paths),
    #path(r'^$', home, name='home'),
    #path(r'^redirect/$', redirect_somewhere, name='home')
]
