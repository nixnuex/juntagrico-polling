# Generated by Django 3.0.2 on 2020-04-27 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juntagrico_polling', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='allow_abstention',
            field=models.BooleanField(default=True, verbose_name='Allow Abstention'),
        ),
    ]
