# Generated by Django 4.2.16 on 2024-12-02 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("game", "0109_create_episodes_23_and_24"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="episode",
            name="indy_worksheet_link",
        ),
        migrations.RemoveField(
            model_name="episode",
            name="lesson_plan_link",
        ),
        migrations.RemoveField(
            model_name="episode",
            name="slides_link",
        ),
        migrations.RemoveField(
            model_name="episode",
            name="student_worksheet_link",
        ),
        migrations.RemoveField(
            model_name="episode",
            name="video_link",
        ),
        migrations.CreateModel(
            name="Worksheet",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "lesson_plan_link",
                    models.CharField(
                        blank=True, default=None, max_length=500, null=True
                    ),
                ),
                (
                    "slides_link",
                    models.CharField(
                        blank=True, default=None, max_length=500, null=True
                    ),
                ),
                (
                    "student_worksheet_link",
                    models.CharField(
                        blank=True, default=None, max_length=500, null=True
                    ),
                ),
                (
                    "indy_worksheet_link",
                    models.CharField(
                        blank=True, default=None, max_length=500, null=True
                    ),
                ),
                (
                    "video_link",
                    models.CharField(
                        blank=True, default=None, max_length=500, null=True
                    ),
                ),
                (
                    "before_level",
                    models.OneToOneField(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="after_worksheet",
                        to="game.level",
                    ),
                ),
                (
                    "episode",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="worksheets",
                        to="game.episode",
                    ),
                ),
            ],
        ),
    ]