from django.shortcuts import render
from .fib import fib

from rest_framework.views import APIView
from rest_framework.response import Response

class FibView(APIView):
    def get(self, request):
        n = int(request.query_params.get('n', '10'))
        fib_n = fib(n)
        return Response({'result': fib_n})
