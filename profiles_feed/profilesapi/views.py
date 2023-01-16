from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from .models import *
from .serializers import *
# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class=ProfileSerializer
    queryset=UserProfile.objects.all()