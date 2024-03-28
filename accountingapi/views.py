from django.forms import CharField
from rest_framework import viewsets
from django.contrib.postgres.aggregates import ArrayAgg
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models.functions import Concat
from django.db.models.functions import Cast

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountTagViewSet(viewsets.ModelViewSet):
    queryset = AccountTag.objects.all()
    serializer_class = AccountTagSerializer

class AccountTypeViewSet(viewsets.ModelViewSet):
    queryset = AccountType.objects.all()
    serializer_class = AccountTypeSerializer

class AccountTypeByCategoryView(viewsets.ModelViewSet):
    queryset = AccountType.objects.all()
    serializer_class = AccountTypeSerializer
    
    # list account types grouped by category
    def list(self, request):
        account_types = AccountType.objects.all()
        account_types_by_category = {}
        for account_type in account_types:
            if account_type.category.name in account_types_by_category:
                account_types_by_category[account_type.category.name].append({
                    'id': account_type.id,
                    'name': account_type.name
                })
            else:
                account_types_by_category[account_type.category.name] = [{
                    'id': account_type.id,
                    'name': account_type.name
                }]
        return Response(account_types_by_category)
    
    
class AccountCategoryViewSet(viewsets.ModelViewSet):
    queryset = AccountCategory.objects.all()
    serializer_class = AccountCategorySerializer

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class AccountTaxViewSet(viewsets.ModelViewSet):
    queryset = AccountTax.objects.all()
    serializer_class = AccountTaxSerializer

class ResCompanyViewSet(viewsets.ModelViewSet):
    queryset = ResCompany.objects.all()
    serializer_class = ResCompanySerializer

class AccountJournalViewSet(viewsets.ModelViewSet):
    queryset = AccountJournal.objects.all()
    serializer_class = AccountJournalSerializer

class AccountMoveLineViewSet(viewsets.ModelViewSet):
    queryset = AccountMoveLine.objects.all()
    serializer_class = AccountMoveLineSerializer

class AccountMoveViewSet(viewsets.ModelViewSet):
    queryset = AccountMove.objects.all()
    serializer_class = AccountMoveSerializer

class AccountGroupViewSet(viewsets.ModelViewSet):
    queryset = AccountGroup.objects.all()
    serializer_class = AccountGroupSerializer
