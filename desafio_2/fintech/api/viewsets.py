from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from fintech.models import Transacao
from .serializers import TransacaooSerializer

class TransacaoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    serializer_class = TransacaooSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('dt_transacao' , 'vl_transacao', 
            'nu_conta_pagador', 'nu_conta_beneficiario', 'dt_transacao')
    lookup_field = 'transaction_id'

    def get_queryset(self):
        # id = self.request.query_params.get('id', None)
        transaction_id = self.request.query_params.get('transaction_id', None)
        dt_transacao = self.request.query_params.get('dt_transacao', None)
        vl_transacao = self.request.query_params.get('vl_transacao', None)
        nu_conta_pagador = self.request.query_params.get('nu_conta_pagador', None)
        nu_conta_beneficiario = self.request.query_params.get('nu_conta_beneficiario', None)
        dt_transacao = self.request.query_params.get('dt_transacao', None)



        queryset = Transacao.objects.all()

        if transaction_id:
            queryset = queryset.filter(transaction_id__iexact=transaction_id)

        if dt_transacao:
            queryset = queryset.filter(dt_transacao__iexact=dt_transacao)

        if vl_transacao:
            queryset = queryset.filter(vl_transacao__iexact=vl_transacao)            

        if nu_conta_pagador:
            queryset = queryset.filter(nu_conta_pagador__iexact=nu_conta_pagador)   

        if nu_conta_beneficiario:
            queryset = queryset.filter(nu_conta_beneficiario__iexact=nu_conta_beneficiario)  

        if dt_transacao:
            queryset = queryset.filter(dt_transacao__iexact=dt_transacao)   


        return queryset

    def list(self, request, *args, **kwargs):
        return super(TransacaoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(TransacaoViewSet, self).create(request, *args, **kwargs)
    
