from django.contrib import admin
from fintech.models import Transacao

@admin.register(Transacao)
class TransacaoAdmin(admin.ModelAdmin):
    list_display = 'transaction_id', 'dt_transacao' , 'vl_transacao', 'nu_conta_pagador', 'nu_conta_beneficiario',
    list_display_links = 'transaction_id',
    search_fields = 'nu_conta_pagador', 'nu_conta_beneficiario',



