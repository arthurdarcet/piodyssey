from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import User


@login_required
def list(request):
    return render(request, 'users/list.html', {
        'users': User.objects.all(),
    })
