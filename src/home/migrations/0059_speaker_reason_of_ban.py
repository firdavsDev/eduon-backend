# Generated by Django 3.0.9 on 2022-02-16 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0058_auto_20220216_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='reason_of_ban',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]