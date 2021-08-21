from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from rest_framework import viewsets
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


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


class helloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ Return a hello message """

        test = ['foo', 'bar', 'baz']
        return Response({'message':'hello world', 'test':test})

    def create(self, request):
        """create a new object"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}!'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

        def retrieve(self, request, pk=None):
            """Handles retrieving an object"""
            return Response({'message':'HTTP Method GET'})

        def update(self, request, pk=None):
            """Handles updating an object"""
            return Response({'HTTP Methon':'PUT'})

        def patrial_update(self, request, pk=None):
            """Handles updating part of an object"""
            return Response({'HTTP Method':'PATCH'})

        def destroy(self, request, pk=None):
            """Handles deleting an object"""
            return Response({'HTTP Method':'Delete'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name','email']


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user Authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
