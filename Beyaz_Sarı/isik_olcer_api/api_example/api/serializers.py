from rest_framework import serializers
# dahili importlar
from api.models import  Library

class LibrarySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120) #modele gelecek olacak verilerin jason formatına çevrilmesi
