# Generated by Django 4.2.2 on 2023-07-23 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='formentry',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='formentry',
            name='phone_no',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='formentry',
            name='roll_no',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='formentry',
            name='preference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.preference'),
        ),
    ]