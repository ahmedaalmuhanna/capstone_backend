from rest_framework import serializers
from reports.models import IOCS, Report
from user.serializers import ProfileSerializer


class IOCSerializer(serializers.ModelSerializer):
    class Meta: 
        model = IOCS
        fields = "__all__"
        
#Serializer to view all info in the report detailed
class ReportListSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    iocs = IOCSerializer()
    class Meta:
        model = Report
        fields = '__all__'        
        
        

#Serializer for everything that has to do with reports excluding the list view
class ReportSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    iocs = IOCSerializer()
    class Meta:
        model = Report
        fields = '__all__'
        
    #https://www.django-rest-framework.org/api-guide/relations/#writable-nested-serializers
    def validate(self, attrs):
        print('validate')
        return super().validate(attrs)
    #To create an IOC within the report serializer on creation of the report
    def create(self, validated_data):
        print(dir(self))
        iocs_data = validated_data.pop('iocs')
        ioc = IOCSerializer(data=iocs_data)
        if ioc.is_valid():
            ioc_object = ioc.save()
        report = Report.objects.create(profile=self.context.get("request").user.profile, iocs=ioc_object, **validated_data)
        return report
    

    #only updating the report side without updating the IOC  
    def update(self, instance, validated_data):        
        instance.title = validated_data.get('title', instance.title)
        instance.reference = validated_data.get('reference', instance.reference)
        instance.details = validated_data.get('details', instance.details)
        instance.save()
        return instance
        