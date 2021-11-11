import investpy
import telegram
from database import DB

user_id = telegram.update.Message.from_user

db = DB()

def ultima_cotacao(acao):
    try:
        dados = investpy.stocks.get_stock_recent_data(acao, 'brazil', order='descending')
        return f'Último preço da {acao.upper()} foi R$ {dados.iloc[0]["Close"]}.'
    except RuntimeError:
        return f'Tente novamente com uma sigla válida.'

def info_acao(acao):
    try:
        info = investpy.stocks.get_stock_information(acao, 'brazil', as_json=True)

        return f"Stock Symbol: {info['Stock Symbol']} \nPrev. Close: {info['Prev. Close']} \nTodays Range: {info['Todays Range']} \nOpen: {info['Open']} \nP/E Ratio: {info['P/E Ratio']}\nDividend (Yield): {info['Dividend (Yield)']} \nNext Earnings Date: {info['Next Earnings Date']}"
   
    except RuntimeError:
        return f'Tente novamente com uma sigla válida.'
    
def cotacao_lista(user_id):
    lista = db.busca_acoes(user_id)
    lista = lista.upper().replace(" ", "").split(",")
    try:
        msg = []
        for acao in lista:
            dados = investpy.stocks.get_stock_recent_data(acao, "brazil", order="descending")
            msg.append('{} - {}'.format(acao, dados.iloc[0]["Close"]))
        return msg
    except RuntimeError:
        return None
    
def add_acao(user_id, acao):
    lista_acoes = db.busca_acoes(user_id)
    if acao not in lista_acoes:
        lista_acoes = lista_acoes + ', ' + acao
    try:
        db.update_list(user_id, lista_acoes)
        return f'Item adicionado'
    except:
        return f'Erro ao adicionar item'
    
def deletar_lista(user_id):
    db.update_list(user_id, '')
    
    