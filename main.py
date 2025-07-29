import os
import logging
from telegram.ext import ApplicationBuilder, CommandHandler
from handlers import (
    start_handler,
    comando_rotina,
    comando_entrada,
    comando_resumo_financeiro,
)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")

def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN não está definido nas variáveis de ambiente.")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CommandHandler("rotina", comando_rotina))
    app.add_handler(CommandHandler("entrada", comando_entrada))
    app.add_handler(CommandHandler("resumo_financeiro", comando_resumo_financeiro))

    print("Bot está ativo e a funcionar ❤️")
    app.run_polling()

if __name__ == "__main__":
    main()