from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import SiteUser
from .serializers import UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = SiteUser.objects.all()
    serializer_class = UserSerializer


class UserObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        check_user = SiteUser.objects.filter(username=username)

        if not check_user:
            return Response({'error': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
        
        response = super(UserObtainAuthToken, self).post(request, *args, **kwargs)
        token = response.data['token']
        user = SiteUser.objects.get(username=username)
        userserializer = UserSerializer(user)
        return Response({'token': token, 'user': userserializer.data})
