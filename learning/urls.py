from django.conf.urls import patterns, url
from learning import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^bab/$', views.bab_view, name='bab'),
        url(r'^bab/(?P<bab_slug>[\w\-]+)/$', views.list_materi, name='materi'), 
        url(r'^materi/(?P<materi_slug>[\w\-]+)/$', views.soal_view, name='soal'), 
        url(r'^tambah_bab/$', views.tambah_bab, name='tambah_bab'), # NEW MAPPING!        
)
       
