from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Question


@login_required
def save_session(request):
    pass
