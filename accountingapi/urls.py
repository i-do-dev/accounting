from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'account-tags', AccountTagViewSet)
router.register(r'account-types', AccountTypeViewSet)
router.register(r'account-taxes', AccountTaxViewSet)
router.register(r'companies', ResCompanyViewSet)
router.register(r'account-journals', AccountJournalViewSet)
router.register(r'account-moveLines', AccountMoveLineViewSet)
router.register(r'account-moves', AccountMoveViewSet)
router.register(r'account-groups', AccountGroupViewSet)
router.register(r'reports', ReportViewSet)
router.register(r'account-categories', AccountCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]