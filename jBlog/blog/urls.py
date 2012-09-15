from django.conf.urls.defaults import patterns,include
#admin.autodiscover()
from views import index,search,upload

asdasd="fck"

urlpatterns = patterns('',
    # Example:
     #(r'^jBlog/', include('jBlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^$',index,{}),
    (r'^search.php$',search),
    (r'^upload.php$',upload),
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #(r'^admin/docz/', settings.MEDIA_ROOT),
    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),
    #(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
    #    'document_root': 'C:/Users/Joran/Documents/joran-django/media/',
    #    }),
    #(r'^(?P<path>.*)$',include('jBlog.blog.urls')),
)
