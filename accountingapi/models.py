import uuid
from django.db import models

from django.db import models

class Account(models.Model):
    #id = models.AutoField(primary_key=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=[
        ('asset', 'Asset'),
        ('liability', 'Liability'),
        ('equity', 'Equity'),
        ('income', 'Income'),
        ('expense', 'Expense'),
    ])
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
    type = models.CharField(max_length=255, choices=[
        ('receivable', 'Receivable'),
        ('payable', 'Payable'),
        ('liquid', 'Liquid'),
        ('fixed', 'Fixed'),
        ('current', 'Current'),
        ('non_current', 'Non-current'),
    ])
    close_method = models.CharField(max_length=255, choices=[
        ('unreconciled', 'Unreconciled'),
        ('detail', 'Detail'),
        ('regular', 'Regular'),
    ])

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
    type = models.CharField(max_length=255, choices=[
        ('sale', 'Sale'),
        ('purchase', 'Purchase'),
        ('cash', 'Cash'),
        ('bank', 'Bank'),
        ('general', 'General'),
    ])
    code = models.CharField(max_length=255)
    default_debit_account_id = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='default_debit_account')
    default_credit_account_id = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='default_credit_account')

class AccountMove(models.Model):
    #id = models.AutoField(primary_key=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    journal_id = models.ForeignKey('AccountJournal', on_delete=models.CASCADE)
    date = models.DateField()
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
