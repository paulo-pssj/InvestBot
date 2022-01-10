def sample_responses(input_text, user_id):
    user_message = str(input_text).lower().strip()

    if user_message in ("oi", "ola", "olá"):
        return "Olá, seja bem vindo ao InvestBrBot."
    
    return "Não estou entendendo! Tente novamente."
