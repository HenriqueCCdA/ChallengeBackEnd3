# Generated by Django 4.0.4 on 2022-04-18 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de importação')),
                ('date', models.DateField(verbose_name='Data da transação')),
            ],
        ),
        migrations.AlterField(
            model_name='transaction',
            name='destination_account',
            field=models.CharField(max_length=100, verbose_name='Banco de origem'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='destination_agency',
            field=models.CharField(max_length=4, verbose_name='Agencia de origem'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='destination_bank',
            field=models.CharField(max_length=100, verbose_name='Banco de origem'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='origin_account',
            field=models.CharField(max_length=7, verbose_name='Agencia de origem'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='origin_agency',
            field=models.CharField(max_length=4, verbose_name='Agencia de origem'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='source_bank',
            field=models.CharField(max_length=100, verbose_name='Banco de origem'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor'),
        ),
    ]
