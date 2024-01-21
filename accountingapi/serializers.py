from rest_framework import serializers
from .models import *

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class AccountTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountTag
        fields = '__all__'

class AccountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountType
        fields = '__all__'

class AccountCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountCategory
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class AccountTaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountTax
        fields = '__all__'

class ResCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResCompany
        fields = '__all__'

class AccountJournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountJournal
        fields = '__all__'

class AccountMoveLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountMoveLine
        fields = '__all__'

class AccountMoveSerializer(serializers.ModelSerializer):
    line_ids = AccountMoveLineSerializer(many=True, read_only=True)

    class Meta:
        model = AccountMove
        fields = '__all__'

class AccountGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountGroup
        fields = '__all__'

