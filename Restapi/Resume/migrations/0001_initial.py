# Generated by Django 3.2.3 on 2021-05-15 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(default='Some String', max_length=100)),
                ('address', models.TextField(default='Some String')),
                ('mobile', models.IntegerField(max_length=15)),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
    ]
