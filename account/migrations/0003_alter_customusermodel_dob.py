# Generated by Django 4.1 on 2022-10-20 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_customusermodel_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='dob',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Birth'),
        ),
    ]
