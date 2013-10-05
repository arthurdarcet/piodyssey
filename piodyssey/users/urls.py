from django.conf.urls import include, patterns, url


urlpatterns = patterns('',
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'users/login.html'}, name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': 'login'}),
    url(
        r'^password/reset$',
        'django.contrib.auth.views.password_reset',
        {
            'post_reset_redirect' : '/password/reset/done',
            'template_name': 'users/password-reset/form.html',
            'email_template_name': 'users/password-reset/email-body.html',
            'subject_template_name': 'users/password-reset/email-subject.txt',
        },
    ),
    url(
        r'^password/reset/done$',
        'django.contrib.auth.views.password_reset_done',
        {'template_name': 'users/password-reset/done.html'},
    ),
    url(
        r'^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)$',
        'django.contrib.auth.views.password_reset_confirm',
        {'post_reset_redirect' : '/password/done', 'template_name': 'users/password-reset/confirm.html'},
        name='password-reset-confirm',
    ),
    url(
        r'^password/done$',
        'django.contrib.auth.views.password_reset_complete',
        {'template_name': 'users/password-reset/complete.html'},
    ),
)
