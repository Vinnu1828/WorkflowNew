# Generated by Django 4.1 on 2022-08-14 14:01

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('holidaydate', models.DateTimeField()),
                ('holidaypurpose', models.CharField(max_length=100, null=True)),
                ('holidaytype', models.CharField(max_length=1)),
                ('status', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'holiday',
            },
        ),
        migrations.CreateModel(
            name='HolidayDepartment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('holidayid', models.IntegerField()),
                ('departmentid', models.IntegerField()),
            ],
            options={
                'db_table': 'holidaydepartment',
            },
        ),
        migrations.CreateModel(
            name='HolidayLocation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('holidayid', models.IntegerField()),
                ('holidaylocation', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'holidaylocation',
            },
        ),
        migrations.CreateModel(
            name='RequestTask',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('requestid', models.IntegerField(null=True)),
                ('taskid', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'requesttask',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('taskname', models.CharField(max_length=100)),
                ('serviceid', models.IntegerField(null=True)),
                ('propertytypeid', models.IntegerField(null=True)),
                ('status', models.CharField(max_length=1)),
                ('dependenttaskid', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'task',
            },
        ),
        migrations.CreateModel(
            name='TaskActivity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('activityname', models.CharField(max_length=100)),
                ('departmentid', models.IntegerField(null=True)),
                ('effortsorginal', models.IntegerField(null=True)),
                ('effortsactual', models.IntegerField(null=True)),
                ('timelineorgnial', models.DecimalField(decimal_places=2, max_digits=3, null=True)),
                ('timelineactual', models.DecimalField(decimal_places=2, max_digits=3, null=True)),
                ('documents', models.CharField(max_length=100, null=True)),
                ('taskactivitycol', models.CharField(max_length=45, null=True)),
            ],
            options={
                'db_table': 'taskactivity',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('teamname', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100, null=True)),
                ('departmentid', models.IntegerField()),
                ('teamlead', models.IntegerField()),
                ('status', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'team',
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('teamid', models.IntegerField()),
                ('employeeid', models.IntegerField()),
            ],
            options={
                'db_table': 'teammember',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('mobileoffice', models.CharField(max_length=15, null=True)),
                ('mobilepersonal', models.CharField(max_length=15, null=True)),
                ('email', models.CharField(max_length=15, null=True)),
                ('departmentid', models.IntegerField(null=True)),
                ('addressline1', models.CharField(max_length=100, null=True)),
                ('addressline2', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('pincode', models.CharField(max_length=20, null=True)),
                ('enablelogin', models.CharField(max_length=1, null=True)),
                ('type', models.CharField(max_length=10, null=True)),
                ('picture', models.BinaryField(null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'employee',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
