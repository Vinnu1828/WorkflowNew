# Generated by Django 4.1.4 on 2022-12-10 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflowapp', '0015_rename_requestdb_request_alter_request_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='requestdate',
            field=models.DateTimeField(null=True),
        ),
    ]