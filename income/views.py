from django.shortcuts import render
from .serializers import IncomeSerializer
# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Income
from rest_framework import permissions
from .permissions import IsOwner


class IncomeListApiView(ListCreateAPIView):
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()
    permission_classes=[permissions.IsAuthenticated]
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
    
class IncomeDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()
    permission_classes=[permissions.IsAuthenticated,IsOwner]
    lookup_field= 'id'
    
    
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)    