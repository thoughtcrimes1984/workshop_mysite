from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^polls/$', 'polls.views.index'),
    (r'^polls/(\d+)/$', 'polls.views.detail'),
    (r'^polls/(\d+)/results/$', 'polls.views.results'),
    (r'^polls/(\d+)/vote/$', 'polls.views.vote'),
)
