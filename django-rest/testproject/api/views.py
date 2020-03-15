from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Secret(APIView):
    def get(self, request, format=None):
        return Response({'secret': 'shrrrr..'})

    def post(self, request, format=None):
        return Response({'secret': 'shrrrr..'})


class NotSecret(APIView):
    def get(self, request, format=None):
        return Response({'public': 'public'})

    def post(self, request, format=None):
        return Response({'public': 'public'})