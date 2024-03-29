from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

class HelloApiView(APIView):
    """Test API Views"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format = None):
        """Returns a list of APIView featurea"""
        an_apiview = [
        'Uses HTTP methods as function'
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self, request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})

        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'medthod':'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})
