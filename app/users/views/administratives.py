from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from ..decorators import administrative_required
from ..forms import AdministrativeSignUpForm
from ..models import User


@method_decorator([administrative_required], name='dispatch')
class SignUpView(CreateView):
    model = User
    form_class = AdministrativeSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'administrative'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('home')


@login_required()
@administrative_required()
def HomeView(request):
    return render(request, 'administratives_HomeView.html')
