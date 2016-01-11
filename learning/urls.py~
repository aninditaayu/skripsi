from django.conf.urls import patterns, url
from learning import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^bab/$', views.bab_view, name='bab'),
        url(r'^bab/(?P<bab_slug>[\w\-]+)/$', views.list_materi, name='materi'), 
        url(r'^bab/(?P<bab_slug>[\w\-]+)/materi/(?P<materi_slug>[\w\-]+)/(?P<soal_id>[\w\-]+)/$', views.soal_view, name='soal'), 
        url(r'^tambah_bab/$', views.tambah_bab, name='tambah_bab'),
	url(r'^register/$', views.register, name='register'),      
	url(r'^login/$', views.user_login, name='login'),
	url(r'^restricted/', views.restricted, name='restricted'),
	url(r'^logout/$', views.user_logout, name='logout'),
	
)
       
