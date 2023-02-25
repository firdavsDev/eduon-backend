# Generated by Django 3.0.9 on 2021-05-27 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_regbonus_summa_full'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='admin',
            name='status',
        ),
        migrations.AddField(
            model_name='admin',
            name='status',
            field=models.ManyToManyField(to='home.Permissions'),
        ),
    ]