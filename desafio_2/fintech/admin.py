from django.contrib import admin
from fintech.models import Transacao

@admin.register(Transacao)
class TransacaoAdmin(admin.ModelAdmin):
    list_display = 'id', 'transaction_id', 'dt_transacao' , 'vl_transacao', 'nu_conta_pagador', 'nu_conta_beneficiario'
    list_display_links = 'id', 'transaction_id'
    search_fields = 'id', 'nu_conta_pagador', 'nu_conta_beneficiario'



