# Generated by Django 4.0.1 on 2022-01-24 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0002_rename_name_email_text_rename_name_password_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='password',
            name='User',
        ),
        migrations.DeleteModel(
            name='Email',
        ),
        migrations.DeleteModel(
            name='Password',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
