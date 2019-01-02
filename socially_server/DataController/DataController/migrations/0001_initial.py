# Generated by Django 2.1.3 on 2018-12-12 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_key', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('time', models.TimeField(default='')),
                ('thing', models.CharField(default='', max_length=60)),
                ('place', models.CharField(default='', max_length=60)),
                ('type', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_key', models.IntegerField(default=0)),
                ('date', models.DateField(verbose_name='date')),
                ('time', models.TimeField(default='', verbose_name='time')),
                ('thing', models.CharField(default='', max_length=60, verbose_name='thing')),
                ('place', models.CharField(default='', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.IntegerField(default=0)),
                ('event_key', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='invitation',
            name='invitee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invitee', to='DataController.User'),
        ),
        migrations.AddField(
            model_name='invitation',
            name='inviter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='DataController.User'),
        ),
        migrations.AddField(
            model_name='calendar',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataController.User'),
        ),
    ]