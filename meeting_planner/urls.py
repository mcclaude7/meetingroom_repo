"""
URL configuration for meeting_planner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from meetings.views import MeetingViewSet, RoomsViewSet, api_interface
#from meetings.views import api_interface
#from meetings. import views

router = DefaultRouter()

router.register('meetings', MeetingViewSet),
router.register('rooms', RoomsViewSet)

#urlpatterns += router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-interface/', api_interface, name='api_interface'),
    # path('api-interface/create-room/', views.create_room, name='create_room'),
    # path('api-interface/create-meeting/', views.create_meeting, name='create_meeting'),

]

