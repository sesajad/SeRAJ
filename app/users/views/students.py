from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from ..decorators import student_required
from ..forms import StudentsSignUpForm
from ..models import User


class SignUpView(CreateView):
    model = User
    form_class = StudentsSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'professor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        user.save()
        return redirect('home')

@login_required()
@student_required()
def HomeView(request):
    return render(request, 'students_HomeView.html')
