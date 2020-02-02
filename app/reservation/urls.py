from django.urls import include, path

from .views import ReservationUpdateStatus, ReservationUpdateView, ReservationListView, CreateReservation

urlpatterns = [
    path('reservations/', include(([
        path('', ReservationListView.as_view() , name='reservation_list'),
        path('create/', CreateReservation.as_view() , name='reservation_create'),
        path('<int:pk>/', ReservationUpdateView.as_view() , name='reservation_view'),
        path('update_status/<int:reservation_pk>', ReservationUpdateStatus, name='reservation_status'),
    ], 'reservation'), namespace='reservations')),

]
