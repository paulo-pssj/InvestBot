# InvestBrBot #
Olá esse projeto tem como objetivo facilitar o acesso aos preços das ações na Bolsa de Valores Brasileira, por meio de um bot do telegram.

# Comandos #

/preco + (sigla da ação) -> Retorna o último preço da ação (ex.: /preco MXRF11);
/lista -> Retorna uma mensagem com o último preço das ações adicionadas a lista;
/add_lista + (siglas das ações) -> Adiciona ações a lista (ex.: /add_lista MXRF11, AAPL34);
/add_acao + (sigla da ação) -> Adiciona uma ação a lista (ex.: /add_acao MGLU3;
/info + (sigla da ação) -> Retorna uma mensagem com informações sobre a ação;
/deletar -> Deleta a lista de ações 

# O que foi utilizado no Projeto #
- Python 3.9
- python-telegram-bot 13.7
- investpy 1.0.7
- sqlite3
