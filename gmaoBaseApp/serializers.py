from dataclasses import field, fields
import imp
from pyexpat import model
from statistics import mode
from rest_framework import serializers
from gmaoBaseApp.models import *


class responsableSerializer(serializers.ModelSerializer):
    class Meta:
        model=responsable
        fields ='__all__'

class techninienSerializer(serializers.ModelSerializer):
    class Meta:
        model=technicine
        fields='__all__'

class pdgSerializer(serializers.ModelSerializer):
    class Meta:
        model=pdg
        fields='__all__'

class brancheSerializer(serializers.ModelSerializer):
    class Meta:
        model=branche
        fields='__all__'

class atelierSerializer(serializers.ModelSerializer):
    class Meta:
        model=Atelier
        fields='__all__'

class machinesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Machines
        fields='__all__'

class cathegorieMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model=CategoriesMachines
        fields='__all__'
        
class InterventionCurativeSerializer(serializers.ModelSerializer):
    class Meta:
        model=IntervenctionCurative
        fields='__all__'
class InterventionPreventiveSerialier(serializers.ModelSerializer):
    class Meta:
        model=InterventionPreventive
        fields='__all__'

class coutSerializer(serializers.ModelSerializer):
    class Meta:
        model=cout
        fields='__all__'
class pieceDeRechargeSerializer(serializers.ModelSerializer):
    class Meta:
        model=pieceDeRechange
        fields='__all__'
    
class categoriePrevetinveSerialzer(serializers.ModelSerializer):
    class Meta:
        model=categoriePreventif
        fields='__all__'

class sousTraitenceSerializer(serializers.ModelSerializer):
    class Meta:
        model=sousTraitence
        fields='__all__'
class magasinSerialzer(serializers.ModelSerializer):
    class Meta:
        model=magasin
        fields='__all__'