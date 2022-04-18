from django.db import models


class Transaction(models.Model):
    source_bank = models.CharField('Banco de origem', max_length=100)
    origin_agency = models.CharField('Agencia de origem', max_length=4)
    origin_account = models.CharField('Agencia de origem', max_length=7)
    destination_bank = models.CharField('Banco de origem', max_length=100)
    destination_agency = models.CharField('Agencia de origem', max_length=4)
    destination_account = models.CharField('Banco de origem', max_length=100)
    transaction_amount = models.DecimalField('Valor', max_digits=10, decimal_places=2)
    transaction_datetime = models.DateTimeField('Date e Hora')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Register(models.Model):
    created_at = models.DateTimeField('Data de importação', auto_now_add=True)
    date = models.DateField('Data da transação')
