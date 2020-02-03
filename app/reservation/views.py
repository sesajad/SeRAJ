from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages


from cal.models import Event
from cal.forms import EventForm

from .models import Reservation
from .forms import CreateReservationForm

from users.decorators import administrative_required

@method_decorator(login_required, name='dispatch')
class CreateReservation(CreateView):
    model = Reservation
    form_class = CreateReservationForm

    template_name = 'reservation/reservation_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        print(self.object.approver_id)
        if not self.object.approver_id is None and \
            not self.object.approver.has_perm('rooms.' + self.object.room.group.approve.codename):
            messages.error(self.request, "Invalid Approver")
            return HttpResponseRedirect(self.request.path_info)

        if self.object.check_overlap(self.object.reserved_start_date.date(), self.object.reserved_start_date.time(), self.object.reserved_end_date.time()):
            messages.error(self.request, "There is time overlap!")
            return HttpResponseRedirect(self.request.path_info)

        self.object.user = self.request.user
        self.object.save()

        return redirect('home')


@method_decorator([login_required], name='dispatch')
class ReservationListView(ListView):
    model = Reservation
    ordering = ('id', )
    context_object_name = 'reservations'
    template_name = 'reservation/reservation_listView.html'

    def get_queryset(self):
        queryset = Reservation.objects.all().filter(status=Reservation.PENDING) \
            .select_related('room')
        return queryset


@method_decorator([login_required], name='dispatch')
class ReservationUpdateView(UpdateView):
    model = Reservation
    fields = ('user', 'room', 'reserved_start_date', 'reserved_end_date', )
    context_object_name = 'reserve'
    template_name = 'reservation/reservation_updateView.html'


    # def get_success_url(self):
    #     return reverse('reservations:reservation_update', kwargs={'pk': self.object.pk})

@login_required()
def ReservationUpdateStatus(request, reservation_pk):
    reservation = get_object_or_404(Reservation, pk=reservation_pk)
    if request.user.has_perm('rooms.%s' % reservation.room.group.own.codename):
        reservation.status = Reservation.ACCEPTED
    elif request.user.has_perm('rooms.%s' % reservation.room.group.approve.codename):
        reservation.status = Reservation.APPROVED
    reservation.save()
    Event.objects.create(title=reservation.title, room=reservation.room, start_time=reservation.reserved_start_date, end_time=reservation.reserved_end_date)

    return HttpResponseRedirect(reverse('reservation:reservation_list'))


@login_required()
def ReservationDecline(request, reservation_pk):
    reservation = get_object_or_404(Reservation, pk=reservation_pk)
    if request.user.has_perm('rooms.%s' % reservation.room.group.own.codename) or \
     request.user.has_perm('rooms.%s' % reservation.room.group.approve.codename):
        reservation.status = Reservation.REJECTED
    reservation.save()
    Event.objects.create(title=reservation.title, room=reservation.room, start_time=reservation.reserved_start_date, end_time=reservation.reserved_end_date)

    return HttpResponseRedirect(reverse('reservation:reservation_list'))
