# Generated by Django 4.1.3 on 2022-11-26 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marvelapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marvel',
            name='comicsname',
        ),
        migrations.RemoveField(
            model_name='marvel',
            name='name',
        ),
        migrations.AddField(
            model_name='marvel',
            name='charactername',
            field=models.CharField(default='', max_length=150),
        ),
    ]
