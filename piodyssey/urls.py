from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from piodyssey.boating import urls as boating_urls


admin.autodiscover()

urlpatterns = patterns('piodyssey.boating',
    url(r'', include(boating_urls)),
)

urlpatterns += patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^login$', 'django.contrib.auth.views.login', {'template_name': 'users/login.html'}),
    (r'^logout$', 'django.contrib.auth.views.logout', {'next_page': 'login'}),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
