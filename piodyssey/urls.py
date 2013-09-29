from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.autodiscover()

urlpatterns = patterns('piodyssey.views',
    url(r'^$', 'index'),
    url(r'^random(?:/(?P<limit>[0-9]+))?$', 'random', name='random-exam'),
)

urlpatterns += patterns('piodyssey.api',
    url(r'api/save-session^$', 'save_session'),
    url(r'api/get-session/(?P<session_id>[0-9]+)^$', 'get_session', name='get-session'),
)

urlpatterns += patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^login$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^logout$', 'django.contrib.auth.views.logout', {'next_page': 'login'}),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
