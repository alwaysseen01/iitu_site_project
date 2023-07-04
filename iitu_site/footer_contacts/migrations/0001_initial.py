# Generated by Django 4.2.2 on 2023-07-03 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactsElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='footer_contacts_icons/')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': "Contacts' elements",
            },
        ),
    ]
