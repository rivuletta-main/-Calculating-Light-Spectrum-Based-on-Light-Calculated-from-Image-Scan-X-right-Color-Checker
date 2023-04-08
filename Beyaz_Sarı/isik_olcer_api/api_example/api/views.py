from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# dahili importlar
from api.models import Library
from api.serializers import LibrarySerializer
from json import dumps, loads
import base64
from io import StringIO
import cv2
from PIL import Image, ImageStat
from django.core.files.base import ContentFile
from datetime import datetime


class LibraryList(APIView):

        def get(self, request):
                print(request.GET["name"])
                libraries=Library.objects.all()
                serializer = LibrarySerializer(libraries, many=True)

                """
                fields = {'name: account_type'}
                libraries = fields
                serializer = LibrarySerializer(libraries, many=True)
                """
                return Response(request.GET["name"])

        def post(self, request):
                print(datetime.now())
                body_unicode = request.body.decode('utf-8')
                #print(body_unicode)
                #data= request.data
                #print(data)
                data = request.POST.get('image', 'Default')
                #print(data)
                format, imgstr = data.split(';base64,') 
                ext = format.split('/')[-1] 
                data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext) # You can save this as file instance.
                im = Image.open(data).convert('L') #yazılan dosyaları okudu ve renklerı grıye çevırdı
                stat = ImageStat.Stat(im) # griye çevrilen resmin stadını aldı.
                print(stat.rms[0]) # griye çevrilen resmin stadını aldı.

                """
                serializer = LibrarySerializer(data=request.data)
                if serializer.is_valid():
                        serializer.save()
                """
                print(datetime.now())
                return Response(stat.rms[0], status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)