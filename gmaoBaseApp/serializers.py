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

class contractSerializer(serializers.ModelSerializer):
    class Meta:
        model=contract
        fields='__all__'

class diplomeSerializer(serializers.ModelField):
    class Meta:
        model=diplome
        fields='__all__'

class formationSerielizer(serializers.ModelSerializer):
    class Meta:
        model=formation
        fields='__all__'


