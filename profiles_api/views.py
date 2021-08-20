from rest_framework.views import APIView
from rest_framework.response import Response


class helloAPIView(APIView):
    """test your APIView"""

    def get(self, request, format=None):
        """returns a list of test features"""

        test = ['foo','bar','baz']

        return Response({'message':'Hello world', 'test':test})
