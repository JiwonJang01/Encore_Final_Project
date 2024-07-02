# Generated by Django 4.1.13 on 2024-07-02 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("diaryapp", "0002_alter_aiwritemodel_images"),
    ]

    operations = [
        migrations.AddField(
            model_name="aiwritemodel",
            name="representative_image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="diaryapp.imagemodel",
            ),
        ),
    ]
