from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from piodyssey.boating import urls as boating_urls
from piodyssey.users import urls as users_urls


admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include(boating_urls)),
    url(r'', include(users_urls)),
)

urlpatterns += patterns('',
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
