from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import JSONParser
from .models import User


# Create your views here.
@api_view(['POST'])
def create_user(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
@api_view(['POST'])
@parser_classes([JSONParser])
def login_user(request):
    if request.method == "POST":
        username = request.data.get('username')
        password = request.data.get('password')


        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Wrong Password')
        

        
        refresh = RefreshToken.for_user(user)

        return Response({
            'message': 'success',
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            })