# Generated by Django 4.2 on 2024-06-27 08:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('room_number', models.PositiveIntegerField()),
                ('remaining_capacity', models.PositiveIntegerField(default=models.PositiveIntegerField())),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(auto_now=True)),
                ('end_date', models.DateField(default=datetime.datetime(2024, 7, 27, 8, 48, 54, 187980, tzinfo=datetime.timezone.utc))),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation_set', to='account.customer')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='reservation', to='room.room')),
            ],
        ),
    ]