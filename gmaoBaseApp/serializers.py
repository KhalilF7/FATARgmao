from dataclasses import field, fields
import imp
from pyexpat import model
from rest_framework import serializers
from gmaoBaseApp.models import *

        
class utilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model=utilisateur
        fields ='__all__'

class responsableSerializer(serializers.ModelSerializer):
    class Meta:
        model=responsable
        fields ='__all__'

class techninienSerialize(serializers.ModelSerializer):
    class Meta:
        model=technicine
        fields='__all__'
