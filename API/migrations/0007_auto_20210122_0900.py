# Generated by Django 3.1.5 on 2021-01-22 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0006_sessions_events'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Kurlar',
        ),
        migrations.AlterModelOptions(
            name='sessions',
            options={},
        ),
        migrations.RemoveField(
            model_name='sessions',
            name='events',
        ),
        migrations.AddField(
            model_name='events',
            name='events',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='API.sessions'),
            preserve_default=False,
        ),
    ]
