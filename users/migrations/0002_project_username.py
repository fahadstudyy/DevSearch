# Generated by Django 4.0.5 on 2022-06-25 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='username',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
