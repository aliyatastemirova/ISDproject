# Generated by Django 3.0.3 on 2020-04-30 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0015_auto_20200430_0559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='what_student_will_learn',
            field=models.TextField(help_text='What Student will learn', null=True),
        ),
    ]
