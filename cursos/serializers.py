from rest_framework import serializers
from .models import Curso,Avaliacao


class CursoSerializer():
    class Meta:
        
        model = Curso
        fields = {
            'id','titulo','url','criacao','ativo',
        }


        def __str__(self):
            return f'{self.nome} avaliou o curso {self.curso} com nota {self.avaliacao}'
        


class AvaliacaoSerializer():
    
    class Meta:
        extra_kwargs = {
            'email': {'write_only':True}
        }
        model = Avaliacao
        fields = {
            'id','curso','nome','email','comentario','avaliacao','criacao','ativo',
        }


        def __str__(self):
            return f'{self.nome} avaliou o curso {self.curso} com nota {self.avaliacao}'