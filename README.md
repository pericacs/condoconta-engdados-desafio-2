<!-- Você trabalha em uma Fintech e nela se tornou necessário acompanhar os dados de pagamentos realizados pelos clientes e registrar os mesmo em um banco de dados transacional. Os pagamentos podem a partir de diversas fontes e, junto da sua liderança, vocês decidiram registrar esse processo através de eventos disparados em uma fila e registrados em uma banco de dados transacional.

Essa parte do teste inclui 3 passos: A primeira parte consiste na criação de um serviço de fila que gerará pagamentos falsos para simular os eventos de pagamentos; a segunda o consumo dos dados do serviço e a terceira o acompanhamento de erros do processo.

1: Criar e Inserir Dados em um Serviço de Fila
Escreva um script na linguagem de programação de sua preferência (Python, Java, etc.) que simule um sistema de execução de pagamentos. O script deve gerar dados fictícios de pagamento e inseri-los em um serviço de fila, como RabbitMQ, Apache Kafka ou AWS SQS. Os dados de pagamento devem incluir pelo menos os seguintes campos: transaction_id, valor, conta do pagador, conta do beneficiário e carimbo de data e hora.

2: Consumir Dados do Serviço de Fila e Escrever em um Banco de Dados Transacional
Escreva outro script na mesma linguagem ou em uma diferente que consuma dados do serviço de fila que você usou no Passo 1 e escreva os dados em um banco de dados transacional, como MySQL, PostgreSQL ou MongoDB. Crie uma tabela ou coleção no banco de dados para armazenar os dados de pagamento. Certifique-se de que os dados sejam escritos atomicamente e lide com possíveis erros ou falhas durante o processo.

3: Tratamento de Erros e Registro
Modifique seu script do Passo 2 para incluir mecanismos de tratamento de erros. Implemente estratégias apropriadas de tratamento de erros para cenários como falhas na conexão com o banco de dados, indisponibilidade do serviço de fila ou formatos de dados inválidos. Você pode escolher registrar os erros no banco de dados se preferir. Utilize uma biblioteca de registro adequada para a linguagem de programação escolhida. -->