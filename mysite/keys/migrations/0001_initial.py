# Generated by Django 4.0.6 on 2022-07-29 07:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('e768ed34-f9eb-43e1-b83e-5d69c1eb0163'), primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]