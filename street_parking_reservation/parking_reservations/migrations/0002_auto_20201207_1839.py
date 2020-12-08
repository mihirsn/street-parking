# Generated by Django 2.2 on 2020-12-07 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_reservations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkingspot',
            name='status',
            field=models.CharField(choices=[('A', 'A'), ('R', 'R'), ('S', 'S')], default=4, max_length=1),
        ),
        migrations.AlterField(
            model_name='parkingspot',
            name='spot_type',
            field=models.IntegerField(choices=[(2, 'Two-wheeler'), (4, 'Four-wheeler')], default='A'),
        ),
    ]