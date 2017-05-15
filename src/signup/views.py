"""simple-signup views

Copyright (c) 2016 Simple is Better Than Complex
Released under MIT license, https://github.com/sibtc/simple-signup/blob/master/LICENSE

Modified:
  - use application configuration
  - detect if server is http/https

"""
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from .forms import SignUpForm
from .tokens import account_activation_token

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate your botw-tracker account'
            message = render_to_string('signup/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
                'protocol': 'https' if request.is_secure() else 'http',
            })
            user.email_user(subject, message)
            return redirect('app-views-signup-activation-sent')
    else:
        form = SignUpForm()
    return render(request, 'signup/signup.html', {'form': form})

def account_activation_sent(request):
    return render(request, 'signup/account_activation_sent.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('')
    else:
        return render(request, 'signup/account_activation_invalid.html')
