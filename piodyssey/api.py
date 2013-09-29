import json

from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Answer, Question, Session


class JsonResponse(HttpResponse):
    def __init__(self, content={}, **kwargs):
        kwargs['content'] = json.dumps(content)
        kwargs['content_type'] = 'application/json'
        super().__init__(**kwargs)


def save_session(request):
    session = Session.objects.create(user=request.user)
    print(request.POST)
    data = json.loads(request.POST.get('answers', '[]'))
    for question_pk, answer in data:
        print(question_pk, answer)
        Answer.objects.create(
            question=Question.objects.get(pk=question_pk),
            answer=answer,
            session=session,
        )
    return redirect(session)

def get_session(request, session_id):
    session = Session.objects.get(id=session_id)
    if not request.user.is_staff and request.user != session.user:
        raise Http404
    return JsonResponse(session.as_dict())

@csrf_exempt
@login_required
def session(request, session_id=None):
    if request.method == 'POST' and session_id is None:
        return save_session(request)
    elif request.method == 'GET' and session_id is not None:
        return get_session(request, session_id)
    else:
        raise Http404
