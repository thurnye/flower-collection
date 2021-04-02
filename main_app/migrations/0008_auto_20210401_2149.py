# Generated by Django 3.1.7 on 2021-04-01 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20210401_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='meal',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='meal',
            name='date',
            field=models.DateField(verbose_name='Period'),
        ),
        migrations.AddField(
            model_name='flower',
            name='flower_vase',
            field=models.ManyToManyField(to='main_app.Vase'),
        ),
    ]