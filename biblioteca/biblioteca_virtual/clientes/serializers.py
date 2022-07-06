from dataclasses import fields
from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('nome', 'idade' , 'rg' ,'cpf', 'email' , 'telefone')