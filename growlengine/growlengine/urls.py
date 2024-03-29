from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#from tastypie.api import Api
#from growl.api import *

#v1_api = Api(api_name='v1')
#v1_api.register(DeveloperResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'growlengine.views.home', name='home'),
    # url(r'^growlengine/', include('growlengine.foo.urls')),

    url(r'^growl/', include('growl.urls')),
    #url(r'^api/', include(v1_api.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
