# Generated by Django 3.0 on 2020-02-12 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0007_auto_20200208_0706'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='date',
            new_name='dateP',
        ),
        migrations.AddField(
            model_name='article',
            name='dateE',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
