from django.db import models
from django.utils import timezone

from users.models import User
from rooms.models import Room
from cal.models import Event

class Reservation(models.Model):
    PENDING = 0
    APPROVED = 1
    ACCEPTED = 2
    DENIED = 3

    STATUS = (
        (PENDING, "Pending"),
        (APPROVED, "Approved"),
        (ACCEPTED, "Accepted"),
        (DENIED, "Denied"),
    )

    title = models.CharField(max_length=200)

    user = models.ForeignKey(User, related_name='owning_req', on_delete=models.CASCADE)
    approver = models.ForeignKey(User, related_name='assigned_req', null=True, on_delete=models.CASCADE)
    participants_gmail = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    status = models.SmallIntegerField(choices=STATUS, default=PENDING)

    reserved_start_date = models.DateTimeField(default=timezone.now)
    reserved_end_date = models.DateTimeField()


    def check_overlap(self, new_date, new_start, new_end):
        overlap = False
        events = Event.objects.filter(room=self.room)
        for event in events:
            if event.start_time.date().day == new_date.day and event.start_time.date().month == new_date.month and event.start_time.date().year == new_date.year:
                if new_start >= event.start_time.time() and new_start <= event.end_time.time():
                    print(1)
                    overlap = True
                    break
                elif new_end >= event.start_time.time() and new_end <= event.end_time.time():
                    overlap = True
                    break
        return overlap
