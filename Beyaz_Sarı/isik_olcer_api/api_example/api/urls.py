from django.urls import path

# dahili importlar
from api.views import  LibraryList

urlpatterns = [

    path('libraries/', LibraryList.as_view()), #burada mecburi olarak views kullanmak zorundayız.

    path('image/', LibraryList.as_view()),

]