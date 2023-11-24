# Generated by Django 4.2.7 on 2023-11-24 04:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("sistema", "0007_alter_emprestimo_livro_info"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usuario",
            name="endereco",
        ),
        migrations.AddField(
            model_name="funcionario",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="usuario",
            name="cidade",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AddField(
            model_name="usuario",
            name="estado",
            field=models.CharField(default="", max_length=2),
        ),
        migrations.AddField(
            model_name="usuario",
            name="numero",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="usuario",
            name="rua",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.DeleteModel(
            name="Endereco",
        ),
    ]
