from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import AccountForms
from .models import Accounts
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .token import token
from django.utils.html import strip_tags
import threading
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
# Create your views here.


# for fasting email
class EmailThread (threading.Thread):
    def __init__(self, html_email):
        self.html_email = html_email
        threading.Thread.__init__(self)

    def run(self):
        return self.html_email.send()


def register(request):
    if request.method == 'POST':
        forms = AccountForms(request.POST)
        sender = settings.EMAIL_HOST_USER
        if forms.is_valid():
            forms.save()
            email = forms.cleaned_data["email"]
            user = Accounts.objects.get(email=email)
            user.is_active = False
            user.save()

            site_address = get_current_site(request)
            html_templates = render_to_string("accounts/email_verifications.html", {
                "user": user,
                "domain": site_address,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": token(user),
            })

            text_content = strip_tags(html_templates)
            html_email = EmailMultiAlternatives(
                "Verify Your Email",
                text_content,
                sender,
                [email]
            )
            html_email.attach_alternative(html_templates, "text/html")
            EmailThread(html_email).start()
            messages.add_message(request, messages.INFO,
                                 "Please verify your Email")
            return redirect('user_login')

    else:
        forms = AccountForms()
    
    return render(request, "accounts/register.html", {
        "forms": forms
    })


def user_login(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]

        auth = authenticate(request, email=email, password=password)
        if auth is not None:
            login(request)
            messages.add_message(request, messages.INFO,
                                 "Login Succesfull")
            return redirect("main")

        else:
            messages.add_message(request, messages.INFO,
                                 "Email or Password is incorect")
            return redirect("user_login")

    else:
        return render(request, "accounts/login.html", {})


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.add_message(request, messages.INFO,
                             "Logout successfull")
        return redirect("main")


def activateUser(request, uid, token):
    if request.method == "GET":

        decodeUID = force_str(urlsafe_base64_decode(uid))

        user = Accounts.objects.get(pk=decodeUID)

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.add_message(request, messages.INFO,
                                 'accounts activated succsefully')
            return redirect('login')
        else:

            messages.add_message(request, messages.INFO,
                                 'try again ')
            return redirect('register')
