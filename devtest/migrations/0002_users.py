from django.contrib.auth.models import User, Group
from django.db import migrations

__author__ = 'npatro'


USERS = ['npatro', 'tgupta', 'ksingh', 'akumar', 'dtewatia',
         'amallik', 'lbhavsar', 'kprasad', 'rsarathi', 'ksuryavanshi',
         'sghosh', 'snarayanan']

USER_GROUPS = {'npatro': 'DEV', 'tgupta': 'ROTO', 'ksingh': 'DEPTH',
               'akumar': 'PAINT', 'dtewatia': 'DEV', 'amallik': 'DEV',
               'lbhavsar': 'RENDER', 'kprasad': 'DEPTH', 'rsarathi': 'PAINT',
               'ksuryavanshi': 'PIPE', 'sghosh': 'PIPE', 'snarayanan': 'PIPE'}

def initialData(apps, schema_editor):
    User.objects.create_superuser(username='admin',
                                  email='admin@gmail.com',
                                  password='secret!')

    for user in USERS:
        u = User.objects.create_user(username=user,
                                     email='%s@gmail.com' % user,
                                     password='secret')
        gp = Group.objects.get(name=USER_GROUPS[user])
        u.groups.add(gp)
        # gp.user_set.add(user)




def reverse(apps, schema_editor):
    User.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
            ('devtest', '0001_groups'),
        ]

    operations = [
        migrations.RunPython(initialData, reverse),
    ]
