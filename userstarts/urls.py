from .views import ExpenseSummaryStarts,IncomeSourcesSummaryStarts
from django.urls import path


urlpatterns = [
    path('expense_category_data', ExpenseSummaryStarts.as_view(), name='expense-category-summery'),
    path('income_sources_data', IncomeSourcesSummaryStarts.as_view(), name='income-sources-summery')
]