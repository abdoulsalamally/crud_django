# Generated by Django 5.0.7 on 2024-07-23 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('ID_USER', models.AutoField(db_column='ID_USER', primary_key=True, serialize=False)),
                ('NOM', models.CharField(db_column='NOM', max_length=100)),
                ('EMAIL', models.EmailField(max_length=254)),
                ('PHONE', models.CharField(db_column='PHONE', max_length=20)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
