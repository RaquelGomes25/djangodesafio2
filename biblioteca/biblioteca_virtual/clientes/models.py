from django.db import models
from  phonenumber_field.modelfields  import  PhoneNumberField
from cpf_field.models import CPFField

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField(max_length=50)
    rg = models.CharField(max_length=15)
    cpf = CPFField('cpf')
    email = models.CharField(max_length=50)
    telefone = PhoneNumberField ()
    
    def _str_(self):
        return self.nome
