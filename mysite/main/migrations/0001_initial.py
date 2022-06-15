# Generated by Django 4.0.3 on 2022-04-19 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parkingspace',
            fields=[
                ('sid', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(db_column='UserName', max_length=80)),
                ('image', models.ImageField(db_column='Image', max_length=200, upload_to='')),
                ('type', models.CharField(db_column='Type', max_length=100)),
                ('city', models.CharField(db_column='City', max_length=100)),
                ('title', models.CharField(db_column='Title', max_length=100)),
                ('price', models.IntegerField(db_column='Price')),
                ('address', models.TextField()),
                ('slots', models.IntegerField(db_column='Slots')),
                ('availslots', models.IntegerField(db_column='AvailSlots')),
                ('discription', models.TextField(db_column='Discription')),
                ('status', models.CharField(db_column='Status', max_length=30)),
            ],
            options={
                'db_table': 'parkingspace',
                'managed': False,
            },
        ),
    ]
