from rest_framework.exceptions import AuthenticationFailed
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
        userSer=techninienSerializer(data=request.data)
        if userSer.is_valid():
            userSer.save()
            return Response({"done"})
        else :
            return Response({"somthing wrong "})


class AuthUser(APIView):
    def post(self,request):
        loginD = request.data['login']
        password = request.data['password']
        userpdg=pdg.objects.filter(login=loginD).first()
        usertech=technicine.objects.filter(username=loginD).first()
        userRes=responsable.objects.filter(username=loginD).first()
        if userpdg is None and userRes is None and usertech is None:
            raise AuthenticationFailed("no user found")
        else:
            if pdgSerializer(userpdg).data['password']==password:
                return Response({"user":"pdg","data":pdgSerializer(userpdg).data})
            elif responsableSerializer(userRes).data["password"]==password:
                return Response({"user":"resp","data":responsableSerializer(userRes).data})
            elif techninienSerializer(usertech).data["password"]==password:
                return Response({"user":"tech","data":techninienSerializer(usertech).data})
            else:
                raise AuthenticationFailed("unvalide password")
