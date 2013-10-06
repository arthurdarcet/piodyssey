from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail as dj_send_mail
from django.shortcuts import Http404, render

from .models import User


@login_required
def users_list(request):
    return render(request, 'users/list.html', {
        'users': User.objects.all(),
    })

@login_required
def send_mail(request, target):
    if target is None:
        target = 'pionniers'
    if target != 'pionniers' and not request.user.is_staff:
        raise Http404
    emails = list(settings.EMAIL_COPY_RECIPIENT)
    if target == 'pionniers' or target == 'all':
        emails += [user.email for user in User.objects.all()]
    if target == 'parents' or target == 'all':
        emails += [user.parents_email for user in User.objects.all()]

    emails = ', '.join(filter(lambda x: x is not None, emails))

    success = error = None
    if request.method == 'POST':
        try:
            dj_send_mail(
                request.POST.get('subject', ''),
                request.POST.get('body'),
                settings.DEFAULT_FROM_EMAIL,
                [emails]
            )
            success = True
        except Exception as e:
            error = str(e)

    return render(request, 'users/send-email.html', {
        'nb_targets': emails.count('@'),
        'body': request.POST.get('body', ''),
        'subject': request.POST.get('subject', ''),
        'error': error,
        'success': success,
    })
