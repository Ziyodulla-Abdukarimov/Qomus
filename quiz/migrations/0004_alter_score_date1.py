# Generated by Django 4.1.3 on 2022-12-04 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_rename_date_score_date1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='date1',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
