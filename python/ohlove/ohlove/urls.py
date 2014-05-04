from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
#admin.autodiscover()

postboxpatterns = patterns('postbox.views',
	url(r'^today$','today_post'),
	url(r'^older/(?P<ndate>.*)$','older_post'),
	url(r'^random/(?P<pid>.*)$','random_post'),
	url(r'^lastest$','lastest_post'),
	url(r'^write$','write'),
	url(r'^$','index'),
)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ohlove.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT }),     

) + postboxpatterns
