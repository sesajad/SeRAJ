from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from .models import Room

from users.decorators import administrative_required

@method_decorator([login_required, administrative_required], name='dispatch')
class CreateRoom(CreateView):
    model = Room
    fields = ('name', 'capacity', )
    template_name = 'room/room_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        return redirect('home')

@method_decorator(login_required, name='dispatch')
class RoomListView(ListView):
    model = Room
    ordering = ('name', )
    context_object_name = 'rooms'
    template_name = 'room/room_listView.html'