# Generated by Django 3.1.6 on 2021-03-25 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('nid', models.IntegerField(unique=True)),
                ('dob', models.DateField()),
                ('cell', models.IntegerField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.TextField()),
                ('isActive', models.BooleanField(default=False)),
                ('isInvestor', models.BooleanField(default=False)),
                ('isEntrepreneur', models.BooleanField(default=False)),
                ('isAnalyst', models.BooleanField(default=False)),
                ('totalInvested', models.FloatField(default=0.0)),
                ('totalWithdrawn', models.FloatField(default=0.0)),
            ],
        ),
    ]
