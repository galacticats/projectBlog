# Generated by Django 3.0 on 2020-02-07 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0003_auto_20200206_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='picture',
            field=models.ImageField(blank='True', default='defaultPic.png', upload_to=''),
        ),
    ]
