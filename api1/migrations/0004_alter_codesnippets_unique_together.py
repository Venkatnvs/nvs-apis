# Generated by Django 4.0.7 on 2023-10-10 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api1', '0003_rename_description_codesnippets_code_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='codesnippets',
            unique_together={('api', 'language')},
        ),
    ]