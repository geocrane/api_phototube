# Generated by Django 2.2.16 on 2022-10-25 10:42

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20221023_1321'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_followers',
        ),
        migrations.RemoveConstraint(
            model_name='follow',
            name='no_self_following',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='following',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='unique_followers'),
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.CheckConstraint(check=models.Q(_negated=True, user=django.db.models.expressions.F('following')), name='no_self_following'),
        ),
    ]
