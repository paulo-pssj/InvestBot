import Acoes

def sample_responses(input_text):
    user_message = str(input_text).lower().strip()

    if user_message in ("oi", "ola", "olá"):
        return "Olá, seja bem vindo ao InvestBrBot."

    elif "preço" in user_message:
        return Acoes.ultima_cotacao(user_message.split(' ')[1])
    
    elif "info" in user_message:
        return Acoes.info_acao(user_message.split(' ')[1])
    
    return "Não estou entendendo! Tente novamente."
