# Generated by Django 4.1.4 on 2022-12-18 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflowapp', '0022_rename_surveynubmber_propertysurvey_surveynumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestschedule',
            name='scheduledt1',
        ),
        migrations.RemoveField(
            model_name='requestschedule',
            name='scheduledt2',
        ),
        migrations.RemoveField(
            model_name='requestschedule',
            name='scheduledt3',
        ),
        migrations.RemoveField(
            model_name='requestschedule',
            name='scheduletime1',
        ),
        migrations.RemoveField(
            model_name='requestschedule',
            name='scheduletime2',
        ),
        migrations.RemoveField(
            model_name='requestschedule',
            name='scheduletime3',
        ),
        migrations.AddField(
            model_name='propertysurvey',
            name='propertyowner',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='requestschedule',
            name='scheduledt',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='requestschedule',
            name='scheduletime',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='requestschedule',
            name='type',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='requestschedule',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='requestschedule',
            name='requestid',
            field=models.IntegerField(null=True),
        ),
    ]
