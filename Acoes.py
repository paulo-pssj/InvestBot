import investpy

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