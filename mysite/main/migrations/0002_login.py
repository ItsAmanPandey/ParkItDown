# Generated by Django 3.2 on 2022-04-20 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('lid', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(db_column='username', max_length=80)),
                ('name', models.CharField(db_column='Name', max_length=50)),
                ('email', models.CharField(db_column='email', max_length=50)),
                ('password', models.CharField(db_column='password', max_length=50)),
            ],
            options={
                'db_table': 'login',
                'managed': True,
            },
        ),
    ]
