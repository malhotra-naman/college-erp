# Generated by Django 3.2.4 on 2022-04-17 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='course_id',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.DO_NOTHING, to='erp_app.courses'),
        ),
    ]
