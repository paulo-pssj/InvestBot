from telegram.ext import *
from commands import *
import constants
import database
import os

db = database.DB()

PORT = int(os.environ.get("PORT", "8443"))

def main():
    updater = Updater(constants.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("lista", lista_command))
    dp.add_handler(CommandHandler("add_lista", add_lista_command))
    dp.add_handler(CommandHandler("add_acao", add_acao_command))
    dp.add_handler(CommandHandler("preco", preco_acao_command))
    dp.add_handler(CommandHandler("deletar", deletar_command))
    dp.add_handler(CommandHandler("info", info_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=constants.API_KEY,
        webhook_url=constants.HEROKU_URL + constants.API_KEY,
    )

    updater.idle()


if __name__ == "__main__":
    db.setup()
    main()
