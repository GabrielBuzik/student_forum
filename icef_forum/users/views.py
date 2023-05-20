from django.http import HttpResponse  
from django.shortcuts import render, redirect  
from django.contrib.auth import login, authenticate  
from .forms import SignupForm  
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_text  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .tokens import account_activation_token  
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.conf import settings


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)  
        if form.is_valid():
            # save form in the memory not in database  
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            # to get the domain of the current site
            current_site = get_current_site(request)
            mail_subject = 'Activation link has been sent to your email id'
            message = render_to_string('users/emails/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                            mail_subject,
                            message,
                            settings.EMAIL_HOST_USER,
                            to=[to_email]
            )
            email.send()
            return render(
                request, 'users/confirmation/confirmation.html', {
                    'text': 'Please confirm your email '
                            'address to complete the registration'
                }
            )
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(
                request, 'users/confirmation/confirmation.html', {
                    'text': 'Thank you for your email confirmation. '
                            'Now you can log in your account.'
                }
            )
    else:
        return render(
                request, 'users/confirmation/confirmation.html', {
                    'text': 'Activation link is invalid!'
                }
            )
