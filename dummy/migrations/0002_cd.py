# Generated by Django 4.0.5 on 2022-07-02 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
