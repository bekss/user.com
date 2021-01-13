# Generated by Django 2.2.12 on 2020-04-26 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('man', '0002_auto_20200417_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='man',
            name='address',
            field=models.CharField(max_length=50, unique=True, verbose_name='Адресс'),
        ),
        migrations.AlterField(
            model_name='man',
            name='body_pass',
            field=models.CharField(max_length=3, verbose_name='Орган, который дал паспорт'),
        ),
        migrations.AlterField(
            model_name='man',
            name='file',
            field=models.FileField(upload_to='media/', verbose_name='Ваше изображение'),
        ),
        migrations.AlterField(
            model_name='man',
            name='fname',
            field=models.CharField(max_length=25, verbose_name='Фамиля'),
        ),
        migrations.AlterField(
            model_name='man',
            name='lname',
            field=models.CharField(max_length=25, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='man',
            name='name',
            field=models.CharField(max_length=25, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='man',
            name='number',
            field=models.CharField(max_length=12, unique=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='man',
            name='number_pass',
            field=models.CharField(max_length=20, unique=True, verbose_name='Номер паспорта'),
        ),
        migrations.AlterField(
            model_name='man',
            name='passport',
            field=models.CharField(choices=[('1', 'ID'), ('2', 'AN'), ('3', 'AC')], max_length=2, verbose_name='Серия паспорта (ID,AC,AN)'),
        ),
        migrations.AlterField(
            model_name='man',
            name='pin',
            field=models.CharField(max_length=6, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='man',
            name='role',
            field=models.CharField(choices=[('1', 'Инструктор'), ('2', 'Координатор'), ('3', 'Регистратор')], max_length=11, verbose_name='Роль'),
        ),
        migrations.AlterField(
            model_name='man',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]