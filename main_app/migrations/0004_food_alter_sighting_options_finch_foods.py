# Generated by Django 4.2.7 on 2023-11-15 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_sighting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='sighting',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='finch',
            name='foods',
            field=models.ManyToManyField(to='main_app.food'),
        ),
    ]