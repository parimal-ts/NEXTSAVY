# Generated by Django 4.2.2 on 2023-06-20 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=1000)),
                ('file', models.FileField(upload_to='files/')),
                ('file_type', models.CharField(max_length=100)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('file_size', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]