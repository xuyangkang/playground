from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication


class Secret(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request, format=None):
        if request.user.is_authenticated:
            print(request.user)
            return Response({'secret': 'this is a secret'})
        else:
            return Response({'secret': 'shrrrr..'})

    def post(self, request, format=None):
        if request.user.is_authenticated:
            print(request.user)
            return Response({'secret': 'this is a secret'})
        else:
            return Response({'secret': 'shrrrr..'})


class NotSecret(APIView):
    def get(self, request, format=None):
        return Response({'public': 'public'})

    def post(self, request, format=None):
        return Response({'public': 'public'})