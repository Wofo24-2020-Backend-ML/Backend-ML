# Generated by Django 3.0.6 on 2020-06-24 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20200624_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Category'),
        ),
    ]
