import re
from traceback import print_tb
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
                data={"userID":pdgSerializer(userpdg).data['id'],"profile":"pdg",}
                return Response({"data":data})
            elif responsableSerializer(userRes).data["password"]==password:
                data = {"userID":responsableSerializer(userRes).data['matricule'],"profile":"res","branche":responsableSerializer(userRes).data['branche']}
                return Response({"data":data})
            elif techninienSerializer(usertech).data["password"]==password:
                data = {"userID":techninienSerializer(usertech).data['matricule'],"profile":"tech","branche":responsableSerializer(userRes).data['branche']}
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
            res=responsable.objects.get(matricule=matricule)
            responsableSer = responsableSerializer(res,data=request.data)
            if responsableSer.is_valid():
                responsableSer.save()
                return Response(responsableSer.data)
        except:
            return Response(responsableSer.errors)
    def delete(self,request,matricule):
        try:
            respon = responsable.objects.get(matricule=matricule)
            print(respon.delete())
            return Response({"message":"deleted"})
        except:
            return Response({"message":"error"}).status_code(404)


class TechniciensApi(APIView):
    def get(self,request):
        try:
            techSer = techninienSerializer(technicine.objects.all(),many=True)
            return Response({"technicines":techSer.data})
        except:
            return Response({"Error":"somthing went wrong"})

    def post(self,request):
        try:
            techSer = techninienSerializer(data=request.data)

            if techSer.is_valid():
                techSer.save()
            return Response(techSer.data)
        except :
            return Response({"message":"somthing want wrong"})


class TechnicienApi(APIView):
    def get(self,request,matricule):
        try:
            techninienSer = techninienSerializer(technicine.objects.get(matricule=matricule))
            return Response({"responsable":techninienSer.data})
        except:
            raise Http404
    def put(self,request,matricule):
        try:
            tech=technicine.objects.get(matricule=matricule)
            techninienSer = techninienSerializer(tech,data=request.data)
            if techninienSer.is_valid():
                techninienSer.save()
                return Response(techninienSer.data)
        except:
            return Response(techninienSer.errors)
    def delete(self,request,matricule):
        try:
            tech = technicine.objects.get(matricule=matricule)
            tech.delete()
            return Response({"message":"deleted"})
        except:
            return Response({"message":"error"}).status_code(404)

class AteliersApi(APIView):
    def get(self,request):
        try:
            ateliers = atelierSerializer(Atelier.objects.all(),many=True)
            return Response(ateliers.data)
        except:
            return Response({"message":"somting went wrong"})
    
    def post(self,request):
        try:
            atelierSer = atelierSerializer(data=request.data)
            if(atelierSer.is_valid()):
                atelierSer.save()
                return Response(atelierSer.data)
        except:
            return Response({"message":"somting went wrong "})
class AtelierApi(APIView):
    def get(self,request,code):
        try:
            atelier = atelierSerializer(Atelier.objects.get(idAtelier=code))
            return Response(atelier)
        except:
            return Response({"message":"somting went wrong"})
    def put(self,request,code):
        try:
            atelier= Atelier.objects.get(idAtelier=code)
            atelierSer = atelierSerializer(atelier,data=request.data)
            if(atelierSer.is_valid()):
                atelierSer.save()
                return Response(atelierSer.data)
        except:
            return Response({"message":"somting went wrong"})
    def delete(self,request,code):
        try:
            atelier=Atelier.objects.get(idAtelier=code)
            atelier.delete()
            return Response({"message":"deleted"})
        except:
            return Response({"message":"somting went wrong"})
        