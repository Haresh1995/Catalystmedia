from django.contrib.auth.models import User
from django.shortcuts import render

def users_view(request):
    users = User.objects.all()
    return render(request, 'user.html', {'users':users})