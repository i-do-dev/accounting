from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'accountTags', AccountTagViewSet)
router.register(r'accountTypes', AccountTypeViewSet)
router.register(r'accountTaxes', AccountTaxViewSet)
router.register(r'resCompanies', ResCompanyViewSet)
router.register(r'accountJournals', AccountJournalViewSet)
router.register(r'accountMoveLines', AccountMoveLineViewSet)
router.register(r'accountMoves', AccountMoveViewSet)
router.register(r'accountGroups', AccountGroupViewSet)
router.register(r'reports', ReportViewSet)
router.register(r'accountCategories', AccountCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]