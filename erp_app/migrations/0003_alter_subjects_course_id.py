# Generated by Django 3.2.4 on 2022-04-17 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp_app', '0002_alter_students_course_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='course_id',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, to='erp_app.courses'),
        ),
    ]
