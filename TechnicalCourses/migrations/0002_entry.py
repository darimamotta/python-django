# Generated by Django 3.2.7 on 2021-09-08 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TechnicalCourses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
    ]
