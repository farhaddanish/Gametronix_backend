
from django import forms
from .models import Accounts
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class AccountForms (UserCreationForm):

    class Meta:
        model = Accounts
        fields = ["first_name", "email", "password1", "password2",]

    def __init__(self, *args, **kwargs):
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


class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.

    """
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = Accounts
        fields = ['email', "password",]

    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Accounts
        fields = ['email', 'password', 'is_active', 'is_admin']

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
