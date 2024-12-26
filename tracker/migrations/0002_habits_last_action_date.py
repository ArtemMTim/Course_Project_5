# Generated by Django 5.1.4 on 2024-12-26 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tracker", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="habits",
            name="last_action_date",
            field=models.DateField(
                blank=True,
                help_text="Введите дату последнего выполнения привычки",
                null=True,
                verbose_name="Дата последнего выполнения привычки",
            ),
        ),
    ]
