# Generated by Django 2.1.2 on 2018-10-21 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referrals', '0005_auto_20181021_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='username',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
