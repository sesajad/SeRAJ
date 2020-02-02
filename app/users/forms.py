from django.contrib.auth.forms import UserCreationForm
from django import forms
from data import consts

from users.models import User

class ProfessorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'department']

    username = forms.EmailField(help_text='use your example@sharif.edu email')
    department = forms.ChoiceField(choices=consts.department_choices, help_text='your department')

    def clean_username(self):
        data = self.cleaned_data['username']
        if not data.endswith('@sharif.edu'):
            raise self.ValidationError("use your example@sharif.edu email")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_professor = True
        user.email = user.username
        if commit:
            user.save()
        return user


class AdministrativeSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        if commit:
            user.save()
        return user
