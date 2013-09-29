import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Answer, Question, Session


class JsonResponse(HttpResponse):
    def __init__(self, content={}, **kwargs):
        super().__init__(content=json.dumps(content), **kwargs)


@login_required
def save_session(request):
    session = Session.objects.create(user=request.user)
    for question_slug, answer in request.POST['answers']:
        Answer.objects.create(
            question=Question.objects.get(slug=question_slug),
            answer=answer,
            session=session,
        )
    return redirect(session)

@login_required
def get_session(request, session_id):
    session = Session.objects.get(id=session_id)
    if not request.user.is_staff and request.user != session.user:
        raise Http404
    return JsonResponse(session.as_dict())
