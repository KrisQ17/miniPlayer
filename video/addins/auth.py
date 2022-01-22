import hashlib

from ..models import User
from django.middleware.csrf import rotate_token
from functools import wraps
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

#decorator about login
def auth(f):
    @wraps(f)
    def wrap(request, *args, **kwargs):
        if '_miniplayer_userid' not in request.session.keys():
            request.session.flush()
            return redirect('login')
        return f(request, *args, **kwargs)
    return wrap

def authenticate(username, password):
    user = None
    try:
        user = User.objects.get(login=username)
        password_hash = hashlib.md5(password.encode('utf-8')).hexdigest()
        if user.password == password_hash:
            return user
        else:
            return None
    except:
        return None

def login(request, user):
    request.session['_miniplayer_userid'] = user._meta.pk.value_to_string(user)
    request.session['username'] = user.name
    rotate_token(request)

def logout(request):
    request.session.flush()