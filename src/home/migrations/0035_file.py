# Generated by Django 3.0.9 on 2021-08-23 09:53

from django.db import migrations, models
import django.db.models.deletion
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_auto_20210818_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('file', models.FileField(default=None, upload_to=home.models.slugify_upload)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Users')),
            ],
        ),
    ]