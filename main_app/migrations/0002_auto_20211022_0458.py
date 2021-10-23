# Generated by Django 3.2.8 on 2021-10-22 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crypto',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='crypto',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('trade_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('quantity', models.IntegerField()),
                ('crypto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.crypto')),
            ],
        ),
    ]
