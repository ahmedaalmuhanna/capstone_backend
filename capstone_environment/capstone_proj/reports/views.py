from reports.serializer import IOCSerializer, ReportSerializer
from reports.models import Report, IOCS
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView,DestroyAPIView, RetrieveAPIView


#IOC model serializers

class IOCCreateView(CreateAPIView):
    serializer_class = IOCSerializer
    # def perform_create(self, serializer):
    #      serializer.save(user=self.request.user)
         
         
class IOCListView(ListAPIView):
    queryset = IOCS.objects.all()
    serializer_class = IOCSerializer


class IOCDetailView(RetrieveAPIView):
    queryset = IOCS.objects.all()
    serializer_class = IOCSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'ioc_id'
    
    
# Report model serializers


#Create report
class ReportCreateView(CreateAPIView):
    serializer_class = ReportSerializer


#List All Reports
class ReportListView(ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    
    
#One Report Detail    
class ReportDetailView(RetrieveAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'report_id'
    
#One Report Update
class ReportUpdateView(UpdateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'report_id'
    
#One Report Delete
class ReportDeleteView(DestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'report_id'