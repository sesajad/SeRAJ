# Generated by Django 3.0 on 2020-02-02 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='department',
            field=models.CharField(blank=True, choices=[('math', 'math'), ('physics', 'physics'), ('ee', 'ee'), ('ce', 'ce'), ('me', 'me'), ('ie', 'ie')], max_length=32),
        ),
        migrations.AddField(
            model_name='room',
            name='resources',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='rules',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
