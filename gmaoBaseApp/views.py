from inspect import classify_class_attrs
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
# Create your views here.
class userView(APIView):
    def get(self,request):
        return Response({"hello"},status=200)
    
    def post(self,request):
        userSer=techninienSerialize(data=request.data)
        if userSer.is_valid():
            userSer.save()
            return Response({"done"})
        else :
            return Response({"somthing wrong "})


class AuthUser(APIView):
    def get(self,request,id):
        userLogin = request.data
        userSer=technicine.objects.get(cin=id)
        return Response(JSONParser().parse(userSer))