from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from .models import Room, RoomGroup

from users.decorators import administrative_required

@method_decorator([login_required, administrative_required], name='dispatch')
class CreateRoom(CreateView):
    model = Room
    fields = ('name', 'capacity', 'rules', 'resources', 'group')
    template_name = 'room/room_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        return redirect('home')


@method_decorator(login_required, name='dispatch')
class RoomGroupListView(ListView):
    model = RoomGroup
    ordering = ('name', )
    context_object_name = 'roomgroups'
    template_name = 'room/roomgroups_listView.html'

@method_decorator(login_required, name='dispatch')
class RoomGroupDetailView(DetailView):
    model = RoomGroup
    context_object_name = 'rg'
    template_name = 'room/room_listView.html'
