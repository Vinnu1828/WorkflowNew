# Generated by Django 4.1.4 on 2022-12-17 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflowapp', '0021_propertysurvey_requestschedule'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propertysurvey',
            old_name='surveynubmber',
            new_name='surveynumber',
        ),
    ]