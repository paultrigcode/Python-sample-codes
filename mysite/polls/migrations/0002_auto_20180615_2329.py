# Generated by Django 2.0 on 2018-06-15 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='pub_choice',
            new_name='pub_date',
        ),
    ]
