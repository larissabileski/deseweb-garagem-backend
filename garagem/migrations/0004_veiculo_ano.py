# Generated by Django 4.1.7 on 2023-03-21 17:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("garagem", "0003_veiculo"),
    ]

    operations = [
        migrations.AddField(
            model_name="veiculo",
            name="ano",
            field=models.IntegerField(default=0),
        ),
    ]