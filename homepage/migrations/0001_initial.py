# Generated by Django 3.2 on 2021-05-13 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todomodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(max_length=50)),
                ('startdate', models.DateField(auto_now=True)),
                ('enddate', models.DateField()),
            ],
        ),
    ]
