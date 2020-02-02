from django.db import models
from django.urls import reverse

from rooms.models import Room

class Event(models.Model):

    title = models.CharField(max_length=200)


    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()




    @property
    def get_html_url(self):
        # url = reverse('cal:event_edit', args=(self.id,))
        return f' {self.title}: {self.start_time.time()}-{self.end_time.time()}</a>'
