# Generated by Django 2.1.2 on 2019-02-16 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kostumerbase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kegiatan_marketingnya',
            name='deskripsi',
            field=models.TextField(),
        ),
    ]