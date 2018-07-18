from django.conf import settings
from django.db import migrations


def apply_migration(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')
    mod_group = Group.objects.create(name='Moderators')
    faucet_request = Permission.objects.get(codename='change_faucetrequest')
    mod_group.permissions.add(faucet_request)


def revert_migration(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.get(name='Moderators').delete()


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0096_auto_20180718_1313'),
    ]

    operations = [
        migrations.RunPython(apply_migration, revert_migration),
    ]