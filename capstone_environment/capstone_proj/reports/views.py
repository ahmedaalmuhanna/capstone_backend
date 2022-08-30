from reports.serializer import IOCSerializer, ReportSerializer
from reports.models import Report, IOCS
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView,DestroyAPIView, RetrieveAPIView


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
    

class ReporCreateView(CreateAPIView):
    serializer_class = ReportSerializer
    