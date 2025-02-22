# https://www.youtube.com/watch?v=vZtm1wuA2yc

from typing import Final
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

from ai import get_response

TOKEN: Final = "5850775739:AAHQJ39gxuCq4f1YMMuEdbkz4LOXaDr-7d8"
BOT_USERNAME: Final = "@MissLunaa_bot"


## Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # To:Do - add logics?
    await update.message.reply_text("Olá!")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # To:Do - add logics?
    await update.message.reply_text("Esteje ajudado! Espero que ajude.")


async def ping_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # To:Do - add logics?
    await update.message.reply_text("pong!")


## Responses
### Lida com as mensagens enviadas
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if "oi" in processed:
        return "Olá! Como você está?"
    return get_response(processed)


### Lida de forma diferente dependendo de onde a mensagem for enviada
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #### Informa se a mensagem vem de um grupo ou pv
    message_type: str = update.message.chat.type

    #### A mensagem em si
    text: str = update.message.text

    #### Mensagem para debug
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    #### Quando em grupos, responde somente se for chamado
    if message_type == "group":
        if BOT_USERNAME in text:
            ##### Remove o username para que o mesmo não seja processado na mensagem
            new_text: str = text.replace(BOT_USERNAME, "").strip()
            response: str = handle_response(new_text)
        else:
            ## testar sem else
            return
    else:
        response: str = handle_response(text)

    print("Bot:", response)
    #### Responde o usuário depois de todo o tratamento
    await update.message.reply_text(response)


## Erros
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")


if __name__ == "__main__":
    print("Starting", BOT_USERNAME)
    app = Application.builder().token(TOKEN).build()

    ## Commands
    ### Delega funções de acordo com o comando
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", ping_command))
    app.add_handler(CommandHandler("ping", ping_command))

    ## Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    ## Erros
    app.add_error_handler(error)

    ## Busca por updates, seja quando um usuário manda mensagem ou um comando
    ### poll_interval em segundos
    print("Polling...")
    app.run_polling(poll_interval=3)
