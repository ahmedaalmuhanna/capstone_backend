"""capstone_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user import views as userViews
from reports import views
from django.views.generic import TemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('register/',userViews.CreateUserAPIView.as_view(), name='register'),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("IOCcreate/", views.IOCCreateView.as_view(), name="IOC-Create"),
    path("IOClist/", views.IOCListView.as_view(), name="IOC-List"),
    path("Reportcreate/", views.ReportCreateView.as_view(), name="Report-Create"),
    path("Reportlist/", views.ReportListView.as_view(), name="Report-list"),
    path("Report/<int:report_id>", views.ReportDetailView.as_view(), name="Report-Detail"),
    path("Reportupdate/<int:report_id>", views.ReportUpdateView.as_view(), name="Report-Update"),
    path("Reportdelete/", views.ReportDeleteView.as_view(), name="Report-Delete"),
    path("home/",TemplateView.as_view(template_name='dashboard/home.html'),name='home' ),
    path('accounts/', include('allauth.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)