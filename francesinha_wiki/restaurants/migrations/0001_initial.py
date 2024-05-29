# Generated by Django 5.0.6 on 2024-05-29 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('francesinhas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('address', models.CharField(max_length=512)),
                ('city', models.CharField(max_length=512)),
                ('country', models.CharField(max_length=512)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=4)),
                ('francesinhas', models.ManyToManyField(related_name='restaurants', to='francesinhas.francesinha')),
            ],
        ),
    ]