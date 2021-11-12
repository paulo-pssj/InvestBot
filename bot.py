from telegram.ext import *
import constants, responses
import Acoes
import database
import os

db = database.DB()

PORT = int(os.environ.get('PORT', '8443'))

def start_command(update, context):
    user_id = update.message.from_user
    db.add_user(user_id['id'], user_id['first_name'])
    update.message.reply_text(f"Olá {user_id['first_name']}, Seja bem vindo ao InvestBrBot. \nDigite /help para ver os comandos disponíveis")

def help_command(update, context):
    update.message.reply_text(constants.comandos)

def handle_message(update, context):
    txt = str(update.message.text)
    user_id = update.message.from_user
    response = responses.sample_responses(txt, user_id)

    update.message.reply_text(response)

def lista_command(update, context):
    user_id = update.message.from_user
    lista = Acoes.cotacao_lista(user_id['id'])
    response = '\n'.join(lista)
    update.message.reply_text(f'{response}')

def add_lista_command(update, context):
    user_id = update.message.from_user
    txt = str(update.message.text)
    db.update_list(user_id['id'], txt.split(' ', maxsplit=1)[1])
    update.message.reply_text('Lista adicionada') 
    
def add_acao_command(update, context):
    user_id = update.message.from_user
    txt = str(update.message.text)
    Acoes.add_acao(user_id['id'], txt.split(' ', maxsplit=1)[1])
    update.message.reply_text('Ação adicionada a lista')

def preco_acao_command(update, context):
    txt = str(update.message.text)
    msg = Acoes.ultima_cotacao(txt.split(' ', maxsplit=1)[1])
    update.message.reply_text(msg)

def deletar_command(update, context):
    user_id = update.message.from_user
    Acoes.deletar_lista(user_id['id'])
    update.message.reply_text('Lista deletada')
    
def info_command(update, context):
    txt = str(update.message.text)
    msg = Acoes.info_acao(txt.split(' ')[1])
    update.message.reply_text(msg)

def error(update, context):
    print(f"Update: {update} caused error: {context.error}")

def main():
    updater = Updater(constants.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('lista', lista_command))
    dp.add_handler(CommandHandler('add_lista', add_lista_command))
    dp.add_handler(CommandHandler('add_acao', add_acao_command))
    dp.add_handler(CommandHandler('preco', preco_acao_command))
    dp.add_handler(CommandHandler('deletar', deletar_command))
    dp.add_handler(CommandHandler('info', info_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    #updater.start_webhook(listen="0.0.0.0",
    #                    port=PORT,
    #                    url_path=constants.API_KEY,
    #                    webhook_url= constants.HEROKU_URL + constants.API_KEY)
    
    updater.start_polling()
    
    
    updater.idle()

if __name__ == '__main__':
    db.setup()
    main()