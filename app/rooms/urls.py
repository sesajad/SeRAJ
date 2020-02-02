from django.urls import include, path

from .views import RoomListView, CreateRoom
from cal.views import calendar_view


urlpatterns = [
    path('rooms/', include(([
        path('', RoomListView.as_view(), name='rooms_list'),
        path('<int:room_pk>/', calendar_view, name='room_view'),
        path('add/', CreateRoom.as_view(), name='room_create'),
    ], 'rooms'), namespace='rooms')),
]

