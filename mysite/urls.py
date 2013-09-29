from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    url(r'^$', 'mysite.blog.views.index'),
    url(r'^update/', 'mysite.blog.views.update'),
    url(r'^delete/', 'mysite.blog.views.delete'),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
