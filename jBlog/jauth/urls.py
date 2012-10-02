__author__ = 'Joran'

from django.conf.urls.defaults import patterns,include
#admin.autodiscover()
from django.utils.html import escape
from views import google_oauth,fb_oauth,login_or_profile

urlpatterns = patterns('',
    # Example:
    #(r'^jBlog/', include('jBlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^login/?$',login_or_profile),
    (r'^login/google/?$',google_oauth),
    (r'^login/fb/?$',fb_oauth),

    #(r'^admin/docz/', settings.MEDIA_ROOT),
    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),
    #(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
    #    'document_root': 'C:/Users/Joran/Documents/joran-django/media/',
    #    }),
    #(r'^(?P<path>.*)$',include('jBlog.blog.urls')),
)

