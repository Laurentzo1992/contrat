# Generated by Django 4.1.2 on 2022-10-22 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gestioncontrat", "0003_alter_travail_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="travail", name="date_signature", field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="travail", name="nature", field=models.CharField(max_length=100),
        ),
    ]