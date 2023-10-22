# Generated by Django 4.1 on 2023-10-22 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0006_category_name_en_category_name_ru_category_name_uz_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_name', to='newsapp.category'),
        ),
    ]