# Generated by Django 3.0.3 on 2020-07-18 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work_orders', '0005_auto_20200716_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='activityid',
        ),
        migrations.CreateModel(
            name='TaskRequiredActivities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activityid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='work_orders.Activities')),
                ('task_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='work_orders.Tasks')),
            ],
        ),
    ]
