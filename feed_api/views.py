from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import filters
from .models import *
from .serializers import *
from .permissions import *

# Create your views here.
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes=(TokenAuthentication,)
    serializer_class=ProfileFeedItemSerializer
    queryset=ProfileFeedItem.objects.all()
    permission_classes=(UpdateOwnStatus,IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)
        return 