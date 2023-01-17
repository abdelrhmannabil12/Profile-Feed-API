from rest_framework import serializers
from .models import *
class ProfileFeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProfileFeedItem
        fields=('id','user_profile','status','created_on',)
        extra_kwargs={'user_profile':{'read_only':True}}