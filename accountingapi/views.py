from rest_framework import viewsets
from .models import *
from .serializers import *

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountTagViewSet(viewsets.ModelViewSet):
    queryset = AccountTag.objects.all()
    serializer_class = AccountTagSerializer

class AccountTypeViewSet(viewsets.ModelViewSet):
    queryset = AccountType.objects.all()
    serializer_class = AccountTypeSerializer

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
