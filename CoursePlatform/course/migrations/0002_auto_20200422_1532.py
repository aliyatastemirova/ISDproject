# Generated by Django 3.0.5 on 2020-04-22 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorialcontent',
            name='file1',
            field=models.FileField(default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='tutorialcontent',
            name='file2',
            field=models.FileField(default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='tutorialcontent',
            name='file3',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]
