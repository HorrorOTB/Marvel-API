# Generated by Django 4.1.3 on 2022-11-26 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marvelapi', '0003_alter_marvel_charactername'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marvel',
            name='charactername',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
