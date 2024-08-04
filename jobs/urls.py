# jobs/urls.py
from django.urls import path
from .views import CompanyCreateView, CompanyDetailView, CompanyListView, JobListCreateView, JobDetailView

urlpatterns = [
    path('jobs/', JobListCreateView.as_view(), name='job-list-create'),
    path('jobs/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('createCompany/', CompanyCreateView.as_view(), name='company-create'),
    path('companyList/', CompanyListView.as_view(), name='company-list'),
    path('company/<int:pk>', CompanyDetailView.as_view(), name='company-detail'),

]
