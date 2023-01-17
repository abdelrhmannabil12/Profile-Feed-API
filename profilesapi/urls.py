from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
from feed_api import views as feedview
router=DefaultRouter()
router.register('profile',views.UserProfileViewSet)
router.register('feed',feedview.UserProfileFeedViewSet)
urlpatterns = [
   path('',include(router.urls)),
   path('login/',views.UserLoginAPIView.as_view()),
]
