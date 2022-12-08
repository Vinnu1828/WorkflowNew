# Generated by Django 4.1 on 2022-08-28 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflowapp', '0005_rename_departmentname_department_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('period', models.IntegerField()),
                ('tax', models.DecimalField(decimal_places=3, max_digits=5)),
                ('status', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'service',
            },
        ),
    ]