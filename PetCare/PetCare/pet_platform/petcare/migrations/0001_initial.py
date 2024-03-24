# Generated by Django 5.0.3 on 2024-03-23 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('petName', models.CharField(choices=[('Cat', 'Cat'), ('Dog', 'Dog'), ('Bird', 'Bird'), ('Rabbit', 'Rabbit'), ('Hamster', 'Hamster')], max_length=100)),
                ('petBreed', models.CharField(max_length=100)),
                ('petInfo', models.TextField()),
                ('petTips', models.TextField()),
                ('imageUrl', models.CharField(max_length=255)),
            ],
        ),
    ]