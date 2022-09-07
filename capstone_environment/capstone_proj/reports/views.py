from multiprocessing import context
from reports.serializer import IOCSerializer, ReportSerializer, ReportListSerializer
from reports.models import Report, IOCS
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView,DestroyAPIView, RetrieveAPIView
from .forms import ReportForm,IOCSForm
from django.shortcuts import render ,redirect
from reports.models import Report
from django.contrib.auth import authenticate 


#IOC model serializers

#Create IOC
class IOCCreateView(CreateAPIView):
    serializer_class = IOCSerializer
    # def perform_create(self, serializer):
    #      serializer.save(user=self.request.user)
         
#List All IOC         
class IOCListView(ListAPIView):
    queryset = IOCS.objects.all()
    serializer_class = IOCSerializer

#Details Of One IOC
class IOCDetailView(RetrieveAPIView):
    queryset = IOCS.objects.all()
    serializer_class = IOCSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'ioc_id'
    
    
#Update One IOC
class IOCUpdateView(UpdateAPIView):
    queryset = IOCS.objects.all()
    serializer_class = IOCSerializer
    lookup_field = 'id'
    lookup_url_kwarg = "ioc_id"
    
    
#Delete One IOC
class IOCDeleteView(DestroyAPIView):
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
    serializer_class = ReportListSerializer
    
    
#One Report Detail    
class ReportDetailView(RetrieveAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportListSerializer
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
    
    
    
# #Specific Profile Report List
# class ProfileReportListView(ListAPIView):
# serializer_class = 


#----------------- Web Part -----------------------#


def report_list(request):
    report = Report.objects.all()
    context = {
        "reports":report
    }
    return render(request,"Report_list.html",context)





def create_report(request):
    form = ReportForm()
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report_form')

    context = {

        "form":form,
    }
    return render(request,"create_report.html",context)




def update_report(request,report_id):
    if not request.user.is_authenticated:
        return redirect("login")

    report = Report.objects.get(id=report_id)
    form = ReportForm(instance=report)
    if request.method == "POST":
       
        form = ReportForm(request.POST, request.FILES,instance=report)
        if form.is_valid():
            form.save()
            return redirect('')
    context = {

        "form":form,
        "report":report,
    }

    return render(request,"update_report.html",context)




# def delete(request,recipe_id):
#     if not request.user.is_authenticated:
#         return redirect("login")
#     recipe = Recipe.objects.get(id =recipe_id)
#     recipe.delete()
#     return redirect('recipes')