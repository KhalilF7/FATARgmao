
import os
from platform import machine
from django.conf import settings
from django.http import Http404, HttpResponseBadRequest
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from FATARgmao.settings import MEDIA_ROOT
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
        motDePasse = request.data['motDePasse']
        userpdg=pdg.objects.filter(login=loginD).first()
        usertech=technicine.objects.filter(login=loginD).first()
        userRes=responsable.objects.filter(login=loginD).first()
        if userpdg is None and userRes is None and usertech is None:
            return Response({"message":"Aucun utilisateur trouver"})
        else:
            if pdgSerializer(userpdg).data['motDePasse']==motDePasse:
                data={"userID":pdgSerializer(userpdg).data['id'],"profile":"pdg",}
                return Response({"data":data})
            elif responsableSerializer(userRes).data["motDePasse"]==motDePasse:
                data = {"userID":responsableSerializer(userRes).data['matricule'],"profile":"res","branche":responsableSerializer(userRes).data['branche']}
                return Response({"data":data})
            elif techninienSerializer(usertech).data["motDePasse"]==motDePasse:
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
            return Response(responsableSer.data)
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
            return Response(responsableSer.data)
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
            return Response(techSer.data)
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
            return Response(techninienSer.data)
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
            return Response(atelier.data)
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


class MachinesApi(APIView):
    def post(self,request):
        try:
            machineSer=machinesSerializer(data=request.data)
            if(machineSer.is_valid()):
                machineSer.save()
                return Response(machineSer.data)
        except Exception as e  :
            return Response({"erreur":"somthing went wrong ","exe":str(e)})
    def get(self,request):
        try:
            machineSer=machinesSerializer(Machines.objects.all(),many=True)
            return Response(machineSer.data)
        except Exception as e  :
            return Response({"error":"somting went wrong","exe":str(e)})
class MachineApi(APIView):
    def get(self,request,code):
        try:
            machine = machinesSerializer(Machines.objects.get(code=code))
            return Response(machine.data)
        except:
            return Response({"message":"somting went wrong"})
    def patch(self,request,code):
        try:
            machine = Machines.objects.get(code=code)
            machinSer = machinesSerializer(machine,data=request.data)
            if(machinSer.is_valid()):
                machinSer.save()
                return Response(machinSer.data)
            print(machinSer.data)
            return Response(machinSer.errors)
        except Exception as e :
            return Response({"message":"somting went wrong","error":str(e)})
    def delete(self,request,code):
        try:    
            machine = Machines.objects.get(code=code)
            file = machine.image
            machine.delete()
            print(file)
            if(file):
                os.remove(os.path.join(settings.MEDIA_ROOT,str(file)))
            return Response({"message":"deleted"})
        except Exception as e :
            return Response({"erreur":"somting went wrong ","exe":str(e)})

class CathergorieMachinesApi(APIView):
    def get(self,request):
        try:
            cathegorieMachineSer=cathegorieMachineSerializer(CategoriesMachines.objects.all(),many=True)
            return Response(cathegorieMachineSer.data)
        except:
            return Response({"message":"somting went wrong"})

class InterventionCurativesApi(APIView):
    def post(self,request):
        try:
            intevetionCurativeSer=InterventionCurativeSerializer(data=request.data)
            if(intevetionCurativeSer.is_valid()):
                intevetionCurativeSer.save()
            return Response(intevetionCurativeSer.data)
        except Exception as e :
            return Response({"message":"somting went wrong","error":str(e)})
    def get(self,request):
        try:
            InterventionCurativeSer=InterventionCurativeSerializer(IntervenctionCurative.objects.all(),many=True)
            return Response(InterventionCurativeSer.data)
        except Exception as e :
            return Response({"message":"somting went wrong ","error":str(e)})

class InterventionsCuratifApi(APIView):
    def get(self,request,code):
        try:
            interventionSer = InterventionCurativeSerializer(IntervenctionCurative.objects.get(codeCuratif=code))
            return Response(interventionSer.data)
        except Exception as e :
            return Response({"message":"somthing went wrong","error":str(e)})
class sousTraitencesApi(APIView):
    def get(self,request):
        try:
            sousTraitenceSer = sousTraitenceSerializer(sousTraitence.objects.all(),many=True)
            return Response(sousTraitenceSer.data)
        except Exception as e :
            return Response({'message':"somting went wrong","error":str(e)})
    def post(self,request):
        try:
            sousTraitenceSer = sousTraitenceSerializer(data=request.data)
            if(sousTraitenceSer.is_valid()):
                sousTraitenceSer.save()
                return Response(sousTraitenceSer.data)
        except Exception as e :
            return Response({"message":"somting went wrong","error":str(e)})