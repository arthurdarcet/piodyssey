import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.html import mark_safe

from .models import Question, Session


@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def random(request, limit):
    return _render(request, Question.objects.order_by('?'), limit)

def _render(request, questions, limit):
    questions = [q.as_dict() for q in questions[:int(limit or 35)]]
    return render(request, 'boating/exam.html', {
        'questions': mark_safe(json.dumps(questions)),
    })

@login_required
def last_sessions(request, limit):
    return render(request, 'boating/last_sessions.html', {
        'sessions': Session.objects.order_by('-created_at')[:int(limit or 20)],
    })

@login_required
def session(request):
    return ''
