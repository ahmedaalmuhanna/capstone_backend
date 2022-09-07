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
from webbrowser import get
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user import views as userViews
from django.views.generic import TemplateView
from user.views import  register_user,login_user,logout_user,dashboard,get_User
from reports.views import report_list,create_report,update_report


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/register/',userViews.CreateUserAPIView.as_view(), name='register'),
    path("api/login/", TokenObtainPairView.as_view(), name="login"),
    path("api/profileupdate/<int:profile_id>", userViews.ProfileUpdateView.as_view(), name="profile-update"),
    path("api/profile/<int:profile_id>", userViews.ProfileDetailView.as_view(), name="profile-detail"),
    # path("api/ioccreate/", views.IOCCreateView.as_view(), name="ioc-create"),
    # path("api/ioclist/", views.IOCListView.as_view(), name="ioc-list"),
    # path("api/ioc/<int:ioc_id>", views.IOCDetailView.as_view(), name="ioc-detail"),
    # path("api/iocupdate/<int:ioc_id>", views.IOCUpdateView.as_view(), name="ioc-update"),
    # path("api/iocdelete/<int:ioc_id>", views.IOCDeleteView.as_view(), name="ioc-delete"),



    # path("api/reportcreate/", views.ReportCreateView.as_view(), name="report-create"),
    # path("api/reportlist/", views.ReportListView.as_view(), name="report-list"),
    # path("api/report/<int:report_id>", views.ReportDetailView.as_view(), name="report-detail"),



    # path("api/reportupdate/<int:report_id>", views.ReportUpdateView.as_view(), name="report-update"),
    # path("api/reportdelete/<int:report_id>", views.ReportDeleteView.as_view(), name="report-delete"),
    # path("api/profile/report/<int:profile_id>", views.ProfileReportListView.as_view(),name='profile-report'),
    path("home/",TemplateView.as_view(template_name='dashboard/home.html'),name='home' ),
    path('accounts/', include('allauth.urls')),
    path("register/", register_user,name="web-register"),
    path("login/", login_user,name="web-login"),
    path("logout/", logout_user,name="web-logout"),
    path("report/", report_list,name="reports"),
    path("dashboard/", get_User,name="web-dashboard"),
    path("dashboard/create-report/", create_report,name="report_form"),
    path("dashboard/update/<int:report_id>/", update_report,name="report_update_form"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)