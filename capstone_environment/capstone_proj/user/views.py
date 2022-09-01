
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from django.contrib.auth.models import User

from reports.models import Report
from .models import Profile
from .serializers import CreateUserSerializer, LoginUserSerializer, ProfileSerializer


# Create your views here.

#User Creation view
class CreateUserAPIView(CreateAPIView):
    serializer_class = CreateUserSerializer
    
#User Login View
class LoginUserAPIView(APIView):
    serializer_class = LoginUserSerializer
    
    def post(self, request):
        my_data = request.data
        serializer = LoginUserSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)
    
    
#User Profile update
class ProfileUpdateView(UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'profile_id'
    
#User

class ProfileDetailView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'profile_id'
    
    # def get_queryset(self):
    #     print(self.kwargs)
    #     profile = self.kwargs['profile_id']
    #     return Report.objects.filter(profile_id=profile)
    