# Generated by Django 3.0.5 on 2020-04-07 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=122)),
                ('date', models.DateField()),
            ],
        ),
    ]
