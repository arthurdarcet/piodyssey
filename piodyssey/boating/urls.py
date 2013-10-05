from django.conf.urls import include, patterns, url


api_patterns = patterns('piodyssey.boating.api',
    url(r'^session(?:/(?P<session_id>[0-9]+))?$', 'session', name='session'),
)

urlpatterns = patterns('piodyssey.boating.views',
    url(r'^$', 'index'),
    url(r'^random(?:/(?P<limit>[0-9]+))?$', 'random', name='random'),
)

urlpatterns += patterns('',
    url(r'^api/', include(api_patterns, namespace='api')),
)
