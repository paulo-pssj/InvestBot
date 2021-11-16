import os
# Token da API fornecida pelo BotFather
API_KEY = '2120245093:AAGC9Pd_Q6-l4O8MGAVbElUiDBWCRSajPc4'
HEROKU_URL = 'https://quiet-waters-54805.herokuapp.com/'
DATABASE_URL = os.environ.get('DATABASE_URL')

comandos = "oi ou olá -> retorna uma saudação;\n \n/preco + (sigla da ação) -> Retorna o último preço da ação (ex: /preco AAPL34);\n \n/add_lista + (Siglas das ações) -> Adiciona itens a listas (ex: /add_lista aapl34, mglu3, mxrf11); \n \n/add_acao + (Sigla da ação) -> Adiciona item a lista (ex: /add_lista aapl34); \n \n/lista -> Retorna o último preço de todas as ações adicionadas na lista; \n \n/deletar -> deleta a lista de ações \n \n/info + (sigla da ação) -> retorna informações da ação (ex: /info AAPL34)."