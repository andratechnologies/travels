# Generated by Django 2.2.16 on 2020-10-11 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consolole', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trassets',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='trassets',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='trassets',
            name='asset_type',
            field=models.IntegerField(),
        ),
    ]
