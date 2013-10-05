import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.html import mark_safe

from .models import Question, Session


@login_required
def random(request, limit):
    return _render(request, Question.objects.order_by('?')[:int(limit or 35)])

def _render(request, questions, session=None):
    return render(request, 'boating/exam.html', {
        'questions': mark_safe(json.dumps([q.as_dict() for q in questions])),
        'session': mark_safe(json.dumps(session.as_dict())) if session is not None else None,
    })

@login_required
def last_sessions(request, limit):
    return render(request, 'boating/last_sessions.html', {
        'sessions': Session.objects.order_by('-created_at')[:int(limit or 20)],
    })

@login_required
def session(request, id):
    session = Session.objects.get_object_or_404(pk=id)
    return _render(
        request,
        [answer.question for answer in session.answers.all()],
        session,
    )
