# Generated by Django 3.0 on 2020-02-07 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0002_article_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='picture',
            field=models.ImageField(blank='True', default='defaultPic.jpg', upload_to=''),
        ),
    ]
