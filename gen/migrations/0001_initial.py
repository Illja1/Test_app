# Generated by Django 4.1.7 on 2023-03-08 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSVData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('column_type', models.CharField(choices=[('1', 'Choose...'), ('2', 'name'), ('3', 'job'), ('4', 'email'), ('5', 'domail'), ('6', 'phone'), ('7', 'company'), ('8', 'text'), ('9', 'integer'), ('9', 'address'), ('10', 'date')], max_length=140)),
                ('order', models.IntegerField(default=0)),
                ('data', models.DateField(auto_now=True)),
            ],
        ),
    ]
