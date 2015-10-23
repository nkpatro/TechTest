from django.contrib.auth.models import Group
from django.db import migrations

__author__ = 'npatro'


GROUPS = ['ROTO', 'DEPTH', 'PAINT', 'DEV', 'PIPE', 'RENDER']


def initialData(apps, schema_editor):
    for group in GROUPS:
        gp = Group(name=group)
        gp.save()
        # Group.objects.create(name=group)


def reverse(apps, schema_editor):
    Group.objects.all().delete()


class Migration(migrations.Migration):
    operations = [
        migrations.RunPython(initialData, reverse),
    ]
