# Generated by Django 3.0.3 on 2020-04-26 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_auto_20200426_0501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorial',
            name='created_by',
        ),
    ]