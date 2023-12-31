# Generated by Django 4.2.6 on 2023-11-10 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=9, verbose_name='Номер автомобиля')),
                ('opisanie', models.TextField(verbose_name='Описание нарушения')),
                ('status', models.CharField(choices=[('рассматривается', 'рассматривается'), ('отклонено', 'отклонено')], default='', max_length=100, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]
