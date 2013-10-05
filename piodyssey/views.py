import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.html import mark_safe

from .boating.models import Session


@login_required
def index(request):
    sessions = Session.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'index.html', {
        'my_sessions': mark_safe(json.dumps([s.score for s in sessions])),
        'show_graph': len(sessions) >= 2,
    })
