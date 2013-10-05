from django.conf.urls import include, patterns, url


urlpatterns = patterns('',
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'users/login.html'}),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': 'login'}),
    url(
        r'^password/reset$',
        'django.contrib.auth.views.password_reset',
        {'post_reset_redirect' : '/password/reset/done'},
    ),
    url(
        r'^password/reset/done$',
        'django.contrib.auth.views.password_reset_done',
    ),
    url(
        r'^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)$',
        'django.contrib.auth.views.password_reset_confirm',
        {'post_reset_redirect' : '/password/done/'},
    ),
    url(
        r'^password/done/$',
        'django.contrib.auth.views.password_reset_complete',
    ),
)
