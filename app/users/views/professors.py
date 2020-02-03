from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from ..decorators import professor_required
from ..forms import ProfessorSignUpForm
from ..models import User


class SignUpView(CreateView):
    model = User
    form_class = ProfessorSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'professor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        gn = 'prof__%s' % user.department
        user.groups.add(Group.objects.get(name=gn))
        user.save()
        return redirect('home')

@login_required()
@professor_required()
def HomeView(request):
    return render(request, 'professor_HomeView.html')
