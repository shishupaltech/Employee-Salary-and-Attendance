# Generated by Django 3.2.12 on 2022-03-24 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esaapp', '0014_auto_20220324_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeedetail',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
