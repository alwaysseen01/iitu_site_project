# Generated by Django 4.2.2 on 2023-06-15 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university_advantages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universityadvantage',
            name='icon',
            field=models.ImageField(upload_to='advantages_icons/'),
        ),
    ]
