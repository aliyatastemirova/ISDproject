# Generated by Django 3.0.3 on 2020-04-30 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0022_auto_20200430_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecontent',
            name='description',
            field=models.TextField(help_text='Detail about this Eposide'),
        ),
        migrations.AlterField(
            model_name='coursecontent',
            name='name',
            field=models.CharField(help_text='Name of the Eposide', max_length=255),
        ),
    ]
