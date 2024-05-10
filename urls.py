from django.urls import path
from .views import create_project, create_deal, deal_tax_credit_transfer

urlpatterns = [
    
    path('create-deal/', create_deal, name='create_deal'),
    path('deal-tax-credit-transfer/<str:deal_name>/', deal_tax_credit_transfer, name='deal_tax_credit_transfer'),
]
