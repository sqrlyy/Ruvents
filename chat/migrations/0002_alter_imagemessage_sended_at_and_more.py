# Generated by Django 4.1 on 2022-08-08 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemessage',
            name='sended_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='imagemessage',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='textmessage',
            name='sended_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='textmessage',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
