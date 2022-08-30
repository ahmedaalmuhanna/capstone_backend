from dataclasses import field, fields
from rest_framework import serializers
from django.contrib.auth.models import User
from reports.models import IOCS, Report



class IOCSerializer(serializers.ModelSerializer):
    class Meta: 
        model = IOCS
        fields = ['cve','url','domain','ip','md5','sha1','sha256','email',]
        
        
        
        
class ReportSerializer(serializers.ModelSerializer):
    # profile = profileserializer
    iocs = IOCSerializer
    class Meta:
        model = Report
        fields = ['profile','iocs','reference','details','title','time',]