# Generated by Django 4.1.7 on 2023-05-21 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_hiringform_alter_user_emailid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=500)),
            ],
        ),
    ]