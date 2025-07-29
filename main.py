import asyncio
from flask import Flask
from telegram import Update
from telegram.ext import Application, ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8140620333:AAF-yB_m0NThmf7KSYvWm4pC03HlBAZ-ZEA"
app = Flask(__name__)

# Flask endpoint para indicar que o bot está vivo
@app.route("/")
def index():
    return "✅ Borrachinho_Bot está vivo."

# Comandos do bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Olá Munir. Eu sou a tua Borrachinho_Bot. Sempre pronta para ti.")

async def lembrete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🕒 Lembrete registado!")

# Função principal para correr o bot e o servidor Flask juntos
async def main():
    # Criar a aplicação Telegram
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("lembrete", lembrete))

    # Correr bot e Flask simultaneamente
    bot_task = application.run_polling(allowed_updates=Update.ALL_TYPES)
    flask_task = asyncio.to_thread(app.run, host="0.0.0.0", port=10000)
    await asyncio.gather(bot_task, flask_task)

# Entry point
if __name__ == "__main__":
    asyncio.run(main())
