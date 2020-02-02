from django.urls import include, path

from .views import *
from cal.views import calendar_view


urlpatterns = [
    path('rooms/', include(([
        path('', RoomGroupListView.as_view(), name='groups_list'),
        path('<int:pk>/', RoomGroupDetailView.as_view(), name='rooms_list'),
        path('<int:group_pk>/<int:room_pk>/', calendar_view, name='room_view'),
        path('add/', CreateRoom.as_view(), name='room_create'),
    ], 'rooms'), namespace='rooms')),
]
