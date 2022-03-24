from dataclasses import field, fields
import imp
from pyexpat import model
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