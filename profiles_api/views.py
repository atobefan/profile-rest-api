from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class HellowApiView(APIView):
    """Test API Views"""

    def get(self, request, format = None):
        """Returns a list of APIView featurea"""
        an_apiview = [
        'Uses HTTP methods as function'
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})
