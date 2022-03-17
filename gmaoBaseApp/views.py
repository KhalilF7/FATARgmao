from uuid import  uuid4
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage

# Create your views here.   
class AuthUser(APIView):
    permission_classes = (AllowAny,)
    @csrf_exempt
    def post(self,request):
        loginD = request.data['login']
        password = request.data['password']
        userpdg=pdg.objects.filter(login=loginD).first()
        usertech=technicine.objects.filter(username=loginD).first()
        userRes=responsable.objects.filter(username=loginD).first()
        if userpdg is None and userRes is None and usertech is None:
            return Response({"message":"Aucun utilisateur trouver"})
        else:
            if pdgSerializer(userpdg).data['password']==password:
                data={"userID":pdgSerializer(userpdg).data['id'],"profile":"pdg"}
                return Response({"data":data})
            elif responsableSerializer(userRes).data["password"]==password:
                data = {"userID":responsableSerializer(userRes).data['matricule'],"profile":"res"}
                return Response({"data":data})
            elif techninienSerializer(usertech).data["password"]==password:
                data = {"userID":techninienSerializer(usertech).data['matricule'],"profile":"tech"}
                return Response({"data":data})
            else:
                return Response({"message":"Mot de passe incorrect"})


class branchesApi(APIView):
    def get(self,request):
        try:
            brancheTable=branche.objects.all()
            brancheSer=brancheSerializer(brancheTable,many=True)
            return Response({"branches":brancheSer.data})
        except:
            return Response({"message":"no row found"})

class ResponsablesApi(APIView):
    @csrf_exempt    

    def get(self,request):
        try:
            responsableSer = responsableSerializer(responsable.objects.all(),many=True)
            return Response({"responsables":responsableSer.data})
        except:
            raise Exception
               
    def post(self,request):
        try:
            responsableSer = responsableSerializer(data=request.data)
            print(request.data)
            if responsableSer.is_valid():
                responsableSer.save()
            return Response(responsableSer.data)
        except :
            return Response({"message":"somthing want wrong"})




class ResponsableApi(APIView):
    def get(self,request,matricule):
        try:
            responsableSer = responsableSerializer(responsable.objects.get(matricule=matricule))
            return Response({"responsable":responsableSer.data})
        except:
            raise Http404
    def put(self,request,matricule):
        try:
            responsableSer = responsableSerializer(responsable.objects.get(matricule=matricule),data=request.data)
            if responsableSer.is_valid():
                responsableSer.save()
                return Response(responsableSer.data)
        except:
            return Response(responsableSer.errors)
    def delete(self,request,matricule):
        try:
            respon = responsable.objects.get(matricule=matricule)
            respon.delete()
            return Response({"message":"deleted"})
        except:
            return Response({"message":"error"}).status_code(404)