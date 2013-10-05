from django.conf.urls import include, patterns, url


api_patterns = patterns('piodyssey.boating.api',
    url(r'^session(?:/(?P<session_id>[0-9]+))?$', 'session', name='session'),
)

urlpatterns = patterns('piodyssey.boating.views',
    url(r'^random(?:/(?P<limit>[0-9]+))?$', 'random', name='random'),
    url(r'^sessions/(?P<id>[0-9]+)$', 'session', name='session'),
    url(r'^sessions/last(?:/(?P<limit>[0-9]+))?$', 'last_sessions', name='last-sessions'),
)

urlpatterns += patterns('',
    url(r'^api/', include(api_patterns, namespace='api')),
)
