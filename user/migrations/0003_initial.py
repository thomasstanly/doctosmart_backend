# Generated by Django 5.0.7 on 2024-08-02 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_image', models.ImageField(upload_to='product')),
                ('product_price', models.IntegerField()),
            ],
        ),
    ]