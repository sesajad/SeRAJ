from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

from rooms.models import RoomGroup, Room
from data.consts import department_choices, room_groups

User = get_user_model()
User.objects.create_superuser('admin', 'sska1377@gmail.com', 'admin')


content_type = ContentType.objects.get_for_model(RoomGroup)
for g in room_groups:
    rg = RoomGroup(name='%s rooms' % g)
    own = Permission.objects.create(
        codename='%s__own' % g,
        name='Owner of %s' % g,
        content_type=content_type,
    )
    own.save()
    approve = Permission.objects.create(
        codename='%s__approve' % g,
        name='Approver of %s' % g,
        content_type=content_type,
    )
    approve.save()
    rg.own = own
    rg.approve = approve
    rg.save()
    for n in range(101, 106):
        r = Room(name='%s %d' % (g, n), capacity=10)
        r.group = rg
        r.save()

for d, _ in department_choices:
    g = Group(name='prof__%s' % d)
    g.save()
    g.permissions.add(Permission.objects.get(codename='%s__approve' % d))
