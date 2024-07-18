# Generated by Django 5.0.1 on 2024-02-16 03:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0002_user_friends_friendshiprequest"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="friendshiprequest",
            constraint=models.UniqueConstraint(
                fields=("created_by", "created_for"), name="unique_constraint"
            ),
        ),
    ]
