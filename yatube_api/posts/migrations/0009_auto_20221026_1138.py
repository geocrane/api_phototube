# Generated by Django 2.2.16 on 2022-10-26 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20221026_0939'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='no_self_following',
        ),
    ]
