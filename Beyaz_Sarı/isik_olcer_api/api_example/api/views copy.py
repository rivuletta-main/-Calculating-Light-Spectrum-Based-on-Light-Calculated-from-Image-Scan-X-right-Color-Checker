from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# dahili importlar
from api.models import Library
from api.serializers import LibrarySerializer

class LibraryList(APIView):

        def get(self, request,name):
                print(name)
                """
                fields = {'name: account_type'}
                libraries = fields
                serializer = LibrarySerializer(libraries, many=True)
                """
                serializer = LibrarySerializer(libraries, many=True)
                return Response(serializer.create())

        def post(self, request,name, format=None):
                print(request.POSTc["id"])
                """
                serializer = LibrarySerializer(data=request.data)
                if serializer.is_valid():
                        serializer.save()
                """
                return Response(request.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)