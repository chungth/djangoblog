from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'mysite.blog.views.index'),
    url(r'^update/', 'mysite.blog.views.update'),
    url(r'^delete/', 'mysite.blog.views.delete'),
)
