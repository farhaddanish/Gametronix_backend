from typing import Any
from django.forms import ModelForm
from .models import Accounts
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class AccountForms (UserCreationForm):

    class Meta:
        model = Accounts
        fields = ["first_name", "email", "password1", "password2",]

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)

        self.fields["first_name"].widget.attrs['class'] = 'input100'
        self.fields["first_name"].widget.attrs.update({'autofocus': 'on'})
        self.fields["first_name"].label = ''

        self.fields["email"].widget.attrs['class'] = "input100"
        self.fields["email"].widget.attrs.pop('autofocus')
        self.fields['email'].label = ''

        self.fields["password1"].widget.attrs['class'] = "input100"
        self.fields["password1"].label = ''

        self.fields["password2"].widget.attrs['class'] = "input100"
        self.fields["password2"].label = ''
