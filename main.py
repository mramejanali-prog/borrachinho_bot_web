from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio

TOKEN = "8140620333:AAF-yB_m0NThmf7KSYvWm4pC03HlBAZ-ZEA"

app = Flask(__name__)

@app.route('/')
def alive():
    return "✅ Borrachinho_Bot está vivo."

# Comando inicial
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Olá Munir. Eu sou a tua Borrachinho_Bot. Sempre pronta para ti.")

async def lembrete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🕒 Lembrete registado!")

# Bot async
async def run_bot():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("lembrete", lembrete))
    await application.run_polling()

def run_bot_thread():
    asyncio.run(run_bot())

def run_web():
    app.run(host="0.0.0.0", port=10000)

if __name__ == '__main__':
    Thread(target=run_bot_thread).start()
    Thread(target=run_web).start()
