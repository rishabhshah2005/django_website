# Generated by Django 3.2.8 on 2021-10-19 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_website', '0011_alter_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.FileField(upload_to=''),
        ),
    ]
