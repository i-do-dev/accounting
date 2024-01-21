import uuid
from django.db import models
from django.utils import timezone

class Account(models.Model):
    #id = models.AutoField(primary_key=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    company_id = models.ForeignKey('ResCompany', on_delete=models.CASCADE)
    account_type_id = models.ForeignKey('AccountType', on_delete=models.CASCADE)
    tax_ids = models.ManyToManyField('AccountTax')
    reconcile = models.BooleanField(default=False)
    note = models.TextField(blank=True)
    deprecated = models.BooleanField(default=False)

class AccountTag(models.Model):
    #id = models.AutoField(primary_key=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    appl_ids = models.ManyToManyField('Account')

class AccountType(models.Model):
    #id = models.AutoField(primary_key=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    close_method = models.CharField(max_length=255, choices=[
        ('unreconciled', 'Unreconciled'),
        ('detail', 'Detail'),
        ('regular', 'Regular'),
    ])
    category = models.ForeignKey('AccountCategory', on_delete=models.CASCADE, null=True)

class AccountCategory(models.Model):
    #id = models.AutoField(primary_key=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    report = models.ForeignKey('Report', on_delete=models.CASCADE)

class Report(models.Model):
    #id = models.AutoField(primary_key=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

class AccountTax(models.Model):
    #id = models.AutoField(primary_key=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    amount = models.FloatField()
    account_id = models.ForeignKey('Account', on_delete=models.CASCADE)

class ResCompany(models.Model):
    #id = models.AutoField(primary_key=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

class AccountJournal(models.Model):
    #id = models.AutoField(primary_key=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    default_debit_account_id = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='default_debit_account')
    default_credit_account_id = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='default_credit_account')

class AccountMove(models.Model):
    #id = models.AutoField(primary_key=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    journal_id = models.ForeignKey('AccountJournal', on_delete=models.CASCADE, related_name='journal', null=True)
    date = models.DateField(default=timezone.now)
    line_ids = models.ManyToManyField('AccountMoveLine')

class AccountMoveLine(models.Model):
    #id = models.AutoField(primary_key=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    move_id = models.ForeignKey('AccountMove', on_delete=models.CASCADE)
    account_id = models.ForeignKey('Account', on_delete=models.CASCADE)
    debit = models.FloatField()
    credit = models.FloatField()

class AccountGroup(models.Model):
    #id = models.AutoField(primary_key=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    from_prefix = models.CharField(max_length=255)
    to_prefix = models.CharField(max_length=255)
    accounts = models.ManyToManyField('Account')
