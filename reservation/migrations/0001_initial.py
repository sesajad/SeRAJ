# Generated by Django 2.2.7 on 2019-11-11 01:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('status', models.SmallIntegerField(choices=[(0, 'Pending'), (1, 'Accepted'), (2, 'Denied')], default=0)),
                ('reserved_start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('reserved_end_date', models.DateTimeField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.Room')),
            ],
        ),
    ]
