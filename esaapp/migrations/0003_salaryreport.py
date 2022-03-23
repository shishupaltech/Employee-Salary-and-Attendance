# Generated by Django 3.2.12 on 2022-03-17 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esaapp', '0002_addemployee'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalaryReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(blank=True, max_length=191, null=True)),
                ('bankAccount', models.BigIntegerField(blank=True, null=True)),
                ('TravelAllowance', models.IntegerField(blank=True, max_length=100, null=True)),
                ('MedicalAllowance', models.IntegerField(blank=True, max_length=100, null=True)),
                ('WashingAllowance', models.IntegerField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
