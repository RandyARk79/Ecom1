# Generated by Django 3.1.5 on 2021-01-10 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20210108_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.CharField(blank=True, default='images/NoImage.jpg', max_length=25),
        ),
    ]