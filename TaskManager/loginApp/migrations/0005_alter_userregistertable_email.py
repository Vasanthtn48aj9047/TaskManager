# Generated by Django 5.1.3 on 2024-11-20 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginApp', '0004_alter_userregistertable_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistertable',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
