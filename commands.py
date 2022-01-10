import constants, responses
import database
import Acoes

db = database.DB()


def start_command(update, context):
    user_id = update.message.from_user
    db.add_user(user_id["id"], user_id["first_name"])
    update.message.reply_text(
        f"Olá {user_id['first_name']}, Seja bem vindo ao InvestBrBot. \nDigite /help para ver os comandos disponíveis"
    )


def help_command(update, context):
    update.message.reply_text(constants.comandos)


def handle_message(update, context):
    txt = str(update.message.text)
    user_id = update.message.from_user
    response = responses.sample_responses(txt, user_id)

    update.message.reply_text(response)


def lista_command(update, context):
    user_id = update.message.from_user
    lista = Acoes.cotacao_lista(user_id["id"])
    response = "\n".join(lista)
    update.message.reply_text(f"{response}")


def add_lista_command(update, context):
    user_id = update.message.from_user
    txt = str(update.message.text)
    db.update_list(user_id["id"], txt.split(" ", maxsplit=1)[1])
    update.message.reply_text("Lista adicionada")


def add_acao_command(update, context):
    user_id = update.message.from_user
    txt = str(update.message.text)
    Acoes.add_acao(user_id["id"], txt.split(" ", maxsplit=1)[1])
    update.message.reply_text("Ação adicionada a lista")


def preco_acao_command(update, context):
    txt = str(update.message.text)
    msg = Acoes.ultima_cotacao(txt.split(" ", maxsplit=1)[1])
    update.message.reply_text(msg)


def deletar_command(update, context):
    user_id = update.message.from_user
    Acoes.deletar_lista(user_id["id"])
    update.message.reply_text("Lista deletada")


def info_command(update, context):
    txt = str(update.message.text)
    msg = Acoes.info_acao(txt.split(" ")[1])
    update.message.reply_text(msg)


def error(update, context):
    print(f"Update: {update} caused error: {context.error}")
