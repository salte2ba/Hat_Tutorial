from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'frisbee.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^registration/', include('registration.urls', namespace = 'registration')),
    url(r'^admin/', include(admin.site.urls)),
)
