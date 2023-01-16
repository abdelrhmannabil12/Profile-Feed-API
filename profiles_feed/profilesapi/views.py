from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from .models import *
from .serializers import *
from .permissions import *
# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class=ProfileSerializer
    queryset=UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email',)