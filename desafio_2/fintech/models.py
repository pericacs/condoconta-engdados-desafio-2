from django.db import models
from faker import Faker
import json
import pika


fake = Faker('pt_BR')

class Transacao(models.Model):
    class Meta:
        verbose_name = 'Transação'
        verbose_name_plural = 'Transações'    

    transaction_id = models.AutoField(primary_key=True)    
    vl_transacao = models.DecimalField(max_digits=10, decimal_places=2)
    nu_conta_pagador = models.CharField(max_length=20, blank=False, null=False)
    nu_conta_beneficiario = models.CharField(max_length=20, blank=False, null=False)
    dt_transacao = models.DateTimeField(auto_now_add=True)



    # @classmethod
    # def save_fake_transaction(cls):
    #     return cls.objects.create(
    #         vl_transacao=fake.pydecimal(left_digits=4, right_digits=2, positive=True),
    #         nu_conta_pagador=fake.random_number(digits=5, fix_len=True),
    #         nu_conta_beneficiario=fake.random_number(digits=5, fix_len=True)    
    #     )   

    @classmethod
    def generate_fake_transaction_queue(cls):
        # # Configurações do RabbitMQ
        rabbitmq_host = 'localhost'
        rabbitmq_port = 5672
        rabbitmq_user = 'guest'
        rabbitmq_password = 'guest'
        exchange_name = 'payments_queue' 
        # Configurar credenciais
        credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_password)
        # Configurar parâmetros de conexão
        connection_params = pika.ConnectionParameters(
            host=rabbitmq_host,
            port=rabbitmq_port,
            credentials=credentials
        )
        # Estabelecer conexão
        connection = pika.BlockingConnection(connection_params)
        # Criar canal
        channel = connection.channel()
        # Declarar troca
        channel.exchange_declare(exchange=exchange_name, exchange_type='direct')

        for _ in range(10):
            transaction_data = {
                'vl_transacao': fake.pydecimal(left_digits=4, right_digits=2, positive=True),
                'nu_conta_pagador': fake.random_number(digits=5, fix_len=True),
                'nu_conta_beneficiario': fake.random_number(digits=5, fix_len=True)
            }
        return channel.basic_publish(
            exchange='',routing_key=exchange_name, body=json.dumps(transaction_data),       
        )   

    @classmethod
    def callback(ch, body):
        # # Configurações do RabbitMQ
        rabbitmq_host = 'localhost'
        rabbitmq_port = 5672
        rabbitmq_user = 'guest'
        rabbitmq_password = 'guest'
        exchange_name = 'payments_queue' 
        # Configurar credenciais
        credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_password)
        # Configurar parâmetros de conexão
        connection_params = pika.ConnectionParameters(
            host=rabbitmq_host,
            port=rabbitmq_port,
            credentials=credentials
        )
        # Estabelecer conexão
        connection = pika.BlockingConnection(connection_params)
        # Criar canal
        channel = connection.channel()
        # Declarar troca
        channel.exchange_declare(exchange=exchange_name, exchange_type='direct')
        # ler arquivo de transação armazenados na fila
        payment_data = json.loads(body.decode('utf-8'))
        try:
            # Salva os dados no banco de dados transacional (Postgres)
            Transacao.objects.create(                
                vl_transacao=payment_data['vl_transacao'],
                nu_conta_pagador=payment_data['nu_conta_pagador'],
                nu_conta_beneficiario=payment_data['nu_conta_beneficiario'],                
            )
            print(f" [x] Recebido Pagamento: {payment_data}")
        except Exception as e:
            print(f" [!] Erro ao salvar no banco de dados: {e}")
      

        # Configuração do consumidor
        channel.basic_consume(queue=exchange_name, on_message_callback=callback, auto_ack=True)        
        channel.start_consuming()




    def __str__(self):
        return  f' {self.nu_conta_pagador} - {self.nm_clinu_conta_beneficiarioente}'  



for _ in range(50):     
    # gerar_transacao = Transacao.save_fake_transaction()
    gerar_transacao_fila = Transacao.generate_fake_transaction_queue()

consumir_transacao = Transacao.callback()