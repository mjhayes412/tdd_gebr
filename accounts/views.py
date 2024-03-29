# import uuid
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.contrib import auth, messages
from accounts.models import Token


def send_login_email(request):
    email = request.POST['email']
    # uid = str(uuid.uuid4())
    token = Token.objects.create(email=email)
    url = request.build_absolute_uri(
        reverse('login') + '?token=' + str(token.uid)
    )
    message_body = f'Use this link to log in:\n\n{url}'
    send_mail(
        'Your login link for gebr',
        message_body,
        'noreply@gebr',
        [email]
    )
    messages.success(
        request,
        "Check your email, we've sent you a link you can use to log in."
    )
    return redirect('/')


def login(request):
    user = auth.authenticate(uid=request.GET.get('token'))
    if user:
        auth.login(request, user)
    return redirect('/')


# def logout(request):
#     auth_logout(request)
#     return redirect('/')
