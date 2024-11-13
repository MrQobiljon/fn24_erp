# Generated by Django 5.1.3 on 2024-11-11 10:46

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=64)),
                ('age', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(5)])),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auth.group')),
            ],
        ),
    ]