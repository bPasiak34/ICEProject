# Generated by Django 4.2.13 on 2024-05-10 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_additionalinfo_id_remove_diagnosis_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paininformation',
            name='type_of_pain',
            field=models.CharField(max_length=50),
        ),
    ]
