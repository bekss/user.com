# Generated by Django 2.2.12 on 2020-05-18 06:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('man', '0005_auto_20200429_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='man',
            name='qrcode',
            field=models.ImageField(blank=True, null=True, upload_to='users/qr-codes', verbose_name='QR code'),
        ),
        migrations.AlterField(
            model_name='man',
            name='birtday',
            field=models.DateField(verbose_name='Туулган жылы'),
        ),
        migrations.AlterField(
            model_name='man',
            name='body_pass',
            field=models.CharField(error_messages={'invalid': 'Введите Орган правильно'}, max_length=12, validators=[django.core.validators.RegexValidator(regex='[A-Z]{2,4}\\s\\d{2,4}-\\d{2,4}$|[A-Z]{2,4}\\s\\d{2,8}$')], verbose_name='Паспортту берген мекеме'),
        ),
        migrations.AlterField(
            model_name='man',
            name='file',
            field=models.FileField(upload_to='media/', verbose_name='Сиздин сурөтуңуз'),
        ),
        migrations.AlterField(
            model_name='man',
            name='fname',
            field=models.CharField(error_messages={'invalid': 'Введите Фамиля на кирилице с главной буквой'}, max_length=25, validators=[django.core.validators.RegexValidator(regex='[А-Я]{1}[а-я]+$|[А-Я]{1}[а-я]+\\s$')], verbose_name='Фамиля'),
        ),
        migrations.AlterField(
            model_name='man',
            name='name',
            field=models.CharField(error_messages={'invalid': 'Введите Имя на кирилице с главной буквой'}, max_length=25, validators=[django.core.validators.RegexValidator(regex='[А-Я]{1}[а-я]+$|[А-Я]{1}[а-я]+\\s$')], verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='man',
            name='number',
            field=models.CharField(error_messages={'invalid': 'Введите правильный номер телефона'}, max_length=12, unique=True, validators=[django.core.validators.RegexValidator(regex='996[0-9]{9}$|996[0-9]{9}$\\s')], verbose_name='Телефон номериниз'),
        ),
        migrations.AlterField(
            model_name='man',
            name='number_pass',
            field=models.CharField(max_length=7, unique=True, verbose_name='Паспорт номери'),
        ),
        migrations.AlterField(
            model_name='man',
            name='passport',
            field=models.CharField(choices=[('1', 'ID'), ('2', 'AN'), ('3', 'AC')], max_length=2, verbose_name='Паспортуңуздун сериясы (ID,AC,AN)'),
        ),
    ]
