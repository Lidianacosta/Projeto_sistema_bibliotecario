# Generated by Django 4.2.7 on 2023-11-25 19:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sistema", "0009_alter_emprestimo_devolucao_data_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="emprestimo",
            name="status",
        ),
        migrations.AlterField(
            model_name="emprestimo",
            name="devolucao_data",
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name="emprestimo",
            name="emprestimo_data",
            field=models.DateField(default=None, null=True),
        ),
    ]
