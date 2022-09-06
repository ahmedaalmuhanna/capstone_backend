
import profile
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from django.contrib.auth.models import User
from .forms import RegisterForm,LoginForm
from django.shortcuts import render ,redirect
from django.contrib.auth import login ,authenticate ,logout
from django.contrib.auth.decorators import login_required #

from reports.models import Report
from .models import Profile
from .serializers import CreateUserSerializer, LoginUserSerializer, ProfileSerializer


# Create your views here.

class CreateUserAPIView(CreateAPIView):
    serializer_class = CreateUserSerializer

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





#-------------------------- web part -----------------------------------#



def register_user(request):
    form = RegisterForm()
    print('pre post')
    if request.method == "POST":
        print('in post condition')
        form = RegisterForm(request.POST)
        if form.is_valid:
            print("in valid stage")
            user = form.save()
            user.set_password(user.password)
            user.save()
            print('logging is user')
            login(request,user)
            return redirect('web-dashboard')
    context = {"form":form,}   
    return render(request,'register.html',context)


def login_user(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            authenticate_user = authenticate(username=username, password=password)
            print('here')
            login(request,authenticate_user)
            return redirect('web-dashboard')
    context = {"form":form}
    return render(request,'login.html',context)

def logout_user(request):
    logout(request)
    return redirect ("login")


def dashboard(request):
     return render(request,'base.html')




def get_User(request):
    users = User.objects.all()
    gov_count = User.objects.filter(profile__is_gov=True).count()
    
    print("here")
    context = {
        "users":users,
        'gov_count': gov_count


    }
    return render (request,"base.html",context)