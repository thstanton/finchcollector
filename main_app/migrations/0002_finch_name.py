# Generated by Django 4.2.7 on 2023-11-13 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='finch',
            name='name',
            field=models.CharField(default='Baz', max_length=100),
            preserve_default=False,
        ),
    ]
