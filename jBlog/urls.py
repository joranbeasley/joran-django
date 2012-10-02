from django.utils.translation import ugettext_lazy as _
from django.conf.urls.defaults import *
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from jBlog.jauth.views import oauth_response as oauth_callback

admin.autodiscover()




urlpatterns = patterns('',
    # Example:
    # (r'^jBlog/', include('jBlog.foo.urls')),
    (r'^oauth/',include('jBlog.jauth.urls')),
    (r'^oath_callback',oauth_callback),
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/docz/', settings.MEDIA_ROOT),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': 'C:/Users/Joran/Documents/joran-django/media/',
        }),
    (r'',include('jBlog.blog.urls')),
)
