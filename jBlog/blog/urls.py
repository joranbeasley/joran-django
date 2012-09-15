from django.conf.urls.defaults import patterns,include
#admin.autodiscover()
from views import index,search,upload_image,view

urlpatterns = patterns('',
    # Example:
     #(r'^jBlog/', include('jBlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^$',index,{}),
    (r'^search.php$',search),
    (r'^upload.php$',upload_image),
    (r'^view/(?P<article_id>.+)/?$',view),
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #(r'^admin/docz/', settings.MEDIA_ROOT),
    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),
    #(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
    #    'document_root': 'C:/Users/Joran/Documents/joran-django/media/',
    #    }),
    #(r'^(?P<path>.*)$',include('jBlog.blog.urls')),
)
