# Generated by Django 3.0 on 2020-02-07 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='picture',
            field=models.ImageField(blank='True', default='defaultPic.png', upload_to=''),
        ),
    ]