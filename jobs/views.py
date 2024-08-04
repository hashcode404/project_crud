from django.forms import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Company, Job
from .serializers import CompanySerializer, JobSerializer

class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def perform_create(self, serializer):
        company_id = self.request.data.get('company')
        if not company_id:
            raise ValidationError({'company': 'This field is required.'})
        company = get_object_or_404(Company, id=company_id)
        serializer.save(posted_by=self.request.user,company=company)

class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class CompanyCreateView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyListView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer