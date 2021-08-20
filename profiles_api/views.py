from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers


class helloAPIView(APIView):
    """test your APIView"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """returns a list of test features"""

        test = ['foo','bar','baz']

        return Response({'message':'Hello world', 'test':test})


    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """Handle updating an object """
        return Response({'method':'put'})


    def patch(self, request, pk=None):
        """Handle partial update of an object"""
        return Response({'method':'patch'})


    def delete(self, request, pk=None):
        """ Handles deletion of an object """
        return Response({'method':'delete'})
