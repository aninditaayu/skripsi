from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 
from registration.backends.simple.views import RegistrationView
from django.http import HttpResponseRedirect

def index(request):
    return HttpResponseRedirect('/learning/')

# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/learning/'
    
urlpatterns = patterns('',

url(r'^admin/', include(admin.site.urls)),
url(r'^$', index),
url(r'^learning/', include('learning.urls')),
url(r'^accounts/', include('registration.backends.simple.urls')),
url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    (r'^accounts/', include('registration.backends.simple.urls')),
	url(r'^sign_up/$', ('learning.views.register_user'), name='daftar'),
	url(r'^register_success/$', ('learning.views.register_success')),    
	url(r'^confirm/(?P<activation_key>\w+)/$', ('learning.views.register_confirm')),  

)


if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )


