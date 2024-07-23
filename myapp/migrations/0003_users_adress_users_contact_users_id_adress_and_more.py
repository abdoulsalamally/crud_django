# Generated by Django 5.0.7 on 2024-07-23 14:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_users_delete_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='users_adress',
            fields=[
                ('ID_ADRESS', models.AutoField(db_column='ID_ADRESS', primary_key=True, serialize=False)),
                ('PROVINCE', models.CharField(db_column='PROVINCE', max_length=100)),
                ('COMMUNE', models.CharField(db_column='COMMUNE', max_length=20)),
            ],
            options={
                'db_table': 'users_adress',
            },
        ),
        migrations.CreateModel(
            name='users_contact',
            fields=[
                ('ID_CONTACT', models.AutoField(db_column='ID_CONTACT', primary_key=True, serialize=False)),
                ('MOBILE_PHONE', models.CharField(db_column='MOBILE_PHONE', max_length=100)),
                ('HOME_PHONE', models.CharField(db_column='HOME_PHONE', max_length=100)),
            ],
            options={
                'db_table': 'users_contact',
            },
        ),
        migrations.AddField(
            model_name='users',
            name='ID_ADRESS',
            field=models.ForeignKey(db_column='ID_ADRESS', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='myapp.users_adress'),
        ),
        migrations.AddField(
            model_name='users',
            name='ID_CONTACT',
            field=models.ForeignKey(db_column='ID_CONTACT', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='myapp.users_contact'),
        ),
    ]