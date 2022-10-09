# Generated by Django 4.1.1 on 2022-10-08 12:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_remove_candidate_branch_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('name', models.CharField(max_length=200, null=True)),
                ('email_id', models.CharField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(max_length=20, null=True)),
                ('div', models.CharField(choices=[('A', 'COMPS A'), ('B', 'COMPS B')], max_length=2, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
