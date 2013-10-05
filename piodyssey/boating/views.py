import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.html import mark_safe

from .models import Question


@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def random(request, limit):
    return _render(request, Question.objects.order_by('?'), limit)

def _render(request, questions, limit):
    questions = [q.as_dict() for q in questions[:int(limit or 35)]]
    return render(request, 'exam.html', {
        'questions': mark_safe(json.dumps(questions)),
    })
