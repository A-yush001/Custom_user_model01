from django.shortcuts import render

# Create your views here.
from .serializers import SignUpSerializer,SigninSerializer
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class SignUpView(generics.GenericAPIView):
    serializer_class=SignUpSerializer


    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response={
                "message":"User created successfully",
                "data":serializer.data
            }

            return Response(data=response,status=status.HTTP_201_CREATED)
        
        return Response(data=None,status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self,request):
        data=request.data
        serializer=SigninSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                "status":"Wrong Credentials",
                "message": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST)
        

        user=authenticate(email=serializer.data['email'],password=serializer.data['password'])

        if user is not None:
            token=Token.objects.get(user=user)
            return Response({
                "message":"Login Successful",
                "token":token.key
            },status=status.HTTP_200_OK)

        else:
            return Response({
                 "message":"invalid credentials"
            },status=status.HTTP_400_BAD_REQUEST)