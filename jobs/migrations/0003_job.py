# Generated by Django 3.1.5 on 2021-01-28 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("jobs", "0002_location")]

    operations = [
        migrations.CreateModel(
            name="Job",
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
                ("title", models.CharField(max_length=200)),
                ("slug", models.SlugField()),
                ("experience", models.PositiveSmallIntegerField()),
                ("salary", models.CharField(blank=True, max_length=50, null=True)),
                ("job_description", models.TextField(blank=True, null=True)),
                ("responsibility", models.TextField(blank=True, null=True)),
                ("others", models.TextField(blank=True, null=True)),
                ("publish", models.BooleanField(default=False)),
                (
                    "location",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="jobs.location",
                    ),
                ),
                (
                    "role",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="jobs.role"
                    ),
                ),
            ],
        )
    ]