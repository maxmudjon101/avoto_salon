# Generated by Django 5.0.2 on 2024-02-29 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avtosalon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avto_nomi', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='news_images/')),
                ('xaqida', models.TextField()),
                ('narxi', models.IntegerField()),
                ('qushimcha_malumot_nomi', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Yangilik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarlavha', models.CharField(max_length=250)),
                ('matn', models.TextField()),
                ('rasmlar', models.ImageField(upload_to='yangilik_rasmlar/')),
                ('yaratilgan_sana', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
