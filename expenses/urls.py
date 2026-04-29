from django.urls import path
from . import views

urlpatterns = [
    path('', views.ExpensListApiView.as_view(), name='expenses'),
    path('<int:id>/', views.ExpensDetailApiView.as_view(), name='expense'),  # ✅ added / and fixed typo
]