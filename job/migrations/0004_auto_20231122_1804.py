# Generated by Django 3.1.3 on 2023-11-22 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_jobs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='recruiter',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='studentuser',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(null=True, upload_to='')),
                ('applydate', models.DateField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.jobs')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.studentuser')),
            ],
        ),
    ]