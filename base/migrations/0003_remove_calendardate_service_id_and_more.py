# Generated by Django 4.1.2 on 2022-10-17 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_agency_id_remove_calendar_id_remove_note_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendardate',
            name='service_id',
        ),
        migrations.RemoveField(
            model_name='route',
            name='agency_id',
        ),
        migrations.RemoveField(
            model_name='stoptime',
            name='stop_id',
        ),
        migrations.RemoveField(
            model_name='stoptime',
            name='stop_note_id',
        ),
        migrations.RemoveField(
            model_name='stoptime',
            name='trip_id',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='route_id',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='service_id',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='shape_id',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='trip_note_id',
        ),
        migrations.AddField(
            model_name='calendardate',
            name='service',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='base.calendar'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='agency',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='base.agency'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stoptime',
            name='stop',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='base.stop'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stoptime',
            name='stop_note',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.note'),
        ),
        migrations.AddField(
            model_name='stoptime',
            name='trip',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='base.trip'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trip',
            name='route',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='base.route'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trip',
            name='service',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='base.calendar'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trip',
            name='shape',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='base.shape'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trip',
            name='trip_note',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.note'),
        ),
    ]
