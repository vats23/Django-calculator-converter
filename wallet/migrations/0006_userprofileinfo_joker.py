# Generated by Django 3.0.8 on 2020-07-28 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0005_auto_20200728_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='joker',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
