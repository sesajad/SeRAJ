from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

from ..decorators import professor_required, administrative_required
from ..forms import ProfessorSignUpForm
from ..models import User



@method_decorator([login_required, administrative_required], name='dispatch')
class ProfessorsSignUpView(CreateView):
    model = User
    form_class = ProfessorSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'professor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('home')

@login_required()
@professor_required()
def HomeView(request):
    return render(request, 'professor_HomeView.html')
