# Generated by Django 2.2.16 on 2020-10-11 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrAssets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('asset_type', models.CharField(max_length=25)),
                ('asset_number', models.CharField(max_length=15)),
                ('asset_model', models.IntegerField(blank=True, null=True)),
                ('asset_value', models.IntegerField(blank=True, default=100000, null=True)),
                ('model_expiry', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/asset_image')),
                ('insurance_expiry_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Assets',
                'verbose_name_plural': 'assets',
                'db_table': 'tr_assets',
            },
        ),
        migrations.CreateModel(
            name='TrConstants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('constant_type', models.CharField(max_length=255)),
                ('value', models.IntegerField()),
                ('label', models.CharField(max_length=255)),
                ('is_editable', models.BooleanField(default=0)),
                ('is_visible', models.BooleanField(default=1)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Constant',
                'verbose_name_plural': 'constant',
                'db_table': 'tr_constants',
            },
        ),
    ]
