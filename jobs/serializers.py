# jobs/serializers.py
from rest_framework import serializers
from .models import Job, Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'location']

class JobSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    posted_by = serializers.ReadOnlyField(source='posted_by.username')

    class Meta:
        model = Job
        fields = ['id', 'title', 'description', 'company', 'location', 'salary', 'created_at', 'updated_at', 'posted_by']

        def create(self, validated_data):
            request = self.context.get("request")

            company_data = validated_data.pop('company')


            company = Company.objects.get(id=company_data.id)
            
            # print(validated_data)


            job = Job.objects.create(company=company, posted_by=request.user, **validated_data)
            return job
