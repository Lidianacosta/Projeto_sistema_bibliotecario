# Generated by Django 4.2.7 on 2023-11-22 01:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("sistema", "0004_rename_first_name_funconario_nome_completo_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="livro",
            old_name="_id",
            new_name="livro_id",
        ),
    ]
