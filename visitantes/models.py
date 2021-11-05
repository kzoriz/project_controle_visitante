from django.db import models
from django.db.models.deletion import PROTECT
#from django.db.models.fields.related import ForeignKey

class Visitante(models.Model):
    nome_completo= models.CharField(verbose_name="Nome completo", max_length=194)
    cpf=models.CharField(verbose_name="CPF",max_length=11)
    data_nascimento=models.DateField(verbose_name="Data de nascimento", auto_now=False, auto_now_add=False)
    numero_casa=models.PositiveIntegerField(verbose_name="Numero da casa a ser visitada")
    placa_veiculo= models.CharField(verbose_name="Placa do veiculo", max_length=7,null= True, blank=True)
    horario_chegada=models.DateTimeField(verbose_name="Horario de chegada na portaria",auto_now_add=True)
    horario_saida= models.DateTimeField(verbose_name="Horario de saida do condominio", auto_now=False, null=True, blank=True)
    horario_autorizacao=models.DateTimeField(verbose_name="Horario de autorização da entrada", auto_now=False, blank=True, null=True)
    morador_responsavel=models.CharField(verbose_name="Nome do morador responsavel por autorizar a entrada", max_length=195, blank=True)
    registrado_por=models.ForeignKey("porteiros.Porteiro",verbose_name= "Porteiro responsavel pelo registro", on_delete= models.PROTECT)
    
    def get_horario_saida(self):
        if self.horario_saida:
            return self.horario_saida
        return "Horário de saída não registrado"

    def get_horario_autorizacao(self):
        if self.horario_autorizacao:
            return self.horario_autorizacao
        return "Visitante aguardando autorização"

    def get_morador_responsavel(self):
        if self.morador_responsavel:
            return self.morador_responsavel
        return "Visitante aguardando autorização"

    def get_placa_veiculo(self):
        if self.placa_veiculo:
            return self.placa_veiculo
        return "Veículo não registrado"


    
    class Meta:
        verbose_name= "Visitante"
        verbose_name_plural= "Visitantes"
        db_table= "visitante"

    def __str__(self):
        return self.nome_completo
