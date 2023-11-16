from django.db import models

class Transacao(models.Model):
    class Meta:
        # criação de indices na base de dados
        indexes = [
            models.Index(fields=['nu_conta_pagador' , 'nu_conta_beneficiario'] )
        ]
        ordering = ('-id',)
        verbose_name = 'Transação'
        verbose_name_plural = 'Transações'    


    transaction_id = models.AutoField(primary_key=True)    
    vl_transacao = models.DecimalField(max_digits=10, decimal_places=2)
    nu_conta_pagador = models.CharField(max_length=20, blank=False, null=False)
    nu_conta_beneficiario = models.CharField(max_length=20, blank=False, null=False)
    dt_transacao = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return  f' Transação da conta  {self.nu_conta_pagador} para a conta 
          {self.nm_clinu_conta_beneficiarioente} no valor de {self.vl_transacao} realizada com sucesso'  
