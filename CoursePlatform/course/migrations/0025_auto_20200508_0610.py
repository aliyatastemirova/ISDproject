# Generated by Django 3.0.3 on 2020-05-08 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0024_auto_20200430_0754'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name_plural': 'Course'},
        ),
        migrations.AlterModelOptions(
            name='coursecontent',
            options={'verbose_name_plural': 'Course Insight'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name_plural': 'SubCategory'},
        ),
    ]
