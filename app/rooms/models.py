from django.db import models
from django.contrib.auth.models import Group, Permission

class RoomGroup(models.Model):
    name = models.CharField(max_length=32)
    own = models.ForeignKey(Permission, on_delete=models.CASCADE, related_name='rg_owns')
    approve = models.ForeignKey(Permission, on_delete=models.CASCADE, related_name='rg_approves')
    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=30)
    capacity = models.IntegerField()
    type = models.CharField(max_length=128)
    rules = models.TextField()
    resources = models.TextField()
    group = models.ForeignKey(RoomGroup, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
