# Generated by Django 5.0.7 on 2024-07-14 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('cargo', models.CharField(max_length=50, verbose_name='cargo')),
            ],
            options={
                'verbose_name': 'Vista Pagina',
                'verbose_name_plural': 'Vista Paginas',
            },
        ),
    ]
