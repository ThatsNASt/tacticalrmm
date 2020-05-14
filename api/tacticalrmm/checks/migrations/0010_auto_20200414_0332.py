# Generated by Django 3.0.5 on 2020-04-14 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0004_auto_20200411_0212'),
        ('checks', '0009_auto_20200414_0328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpuloadcheck',
            name='task_on_failure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cpuloadtaskfailure', to='automation.AutomatedTask'),
        ),
        migrations.AlterField(
            model_name='diskcheck',
            name='task_on_failure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='disktaskfailure', to='automation.AutomatedTask'),
        ),
        migrations.AlterField(
            model_name='pingcheck',
            name='task_on_failure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pingtaskfailure', to='automation.AutomatedTask'),
        ),
        migrations.AlterField(
            model_name='scriptcheck',
            name='task_on_failure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='scripttaskfailure', to='automation.AutomatedTask'),
        ),
        migrations.AlterField(
            model_name='winservicecheck',
            name='task_on_failure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='winsvctaskfailure', to='automation.AutomatedTask'),
        ),
    ]