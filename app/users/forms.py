from django.contrib.auth.forms import UserCreationForm

from users.models import User

class ProfessorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_Professor = True
        if commit:
            user.save()
        return user


class AdministrativeSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_Administrative = True
        if commit:
            user.save()
        return user
