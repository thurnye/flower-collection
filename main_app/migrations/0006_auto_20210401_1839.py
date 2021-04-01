# Generated by Django 3.1.7 on 2021-04-01 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20210401_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='growth',
            field=models.CharField(choices=[('', 'Sunlight'), ('', 'Proper Temperature'), ('', 'Moisture'), ('', 'Air'), ('', 'Nutrients')], default='', max_length=50),
        ),
    ]
