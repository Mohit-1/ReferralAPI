# Generated by Django 2.1.2 on 2018-10-21 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('referrals', '0003_auto_20181021_1009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='referral',
            old_name='referral_code',
            new_name='referrer',
        ),
    ]