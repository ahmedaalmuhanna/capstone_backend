from dataclasses import field, fields
import profile
from rest_framework import serializers
from reports.models import IOCS, Report
from user.serializers import ProfileSerializer



class IOCSerializer(serializers.ModelSerializer):
    class Meta: 
        model = IOCS
        fields = "__all__"
        
        
        
        
class ReportSerializer(serializers.ModelSerializer):
    # profile = serializers.SerializerMethodField()
    # def get_profile(self, obj):
    #     return ProfileSerializer(obj.profile).data 
    profile = ProfileSerializer
    iocs = IOCSerializer()
    class Meta:
        model = Report
        # fields = ['profile','iocs','reference','details','title',]
        fields = '__all__'
        
        
        #https://www.django-rest-framework.org/api-guide/relations/#writable-nested-serializers
        
    def create(self, validated_data):
        iocs_data = validated_data.pop('iocs')
        ioc = IOCSerializer(data=iocs_data)
        if ioc.is_valid():
            ioc_object = ioc.save()
        report = Report.objects.create(iocs=ioc_object, **validated_data)
        return report