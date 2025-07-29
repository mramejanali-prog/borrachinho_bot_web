from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, ContextTypes
)

TOKEN = "8140620333:AAF-yB_m0NThmf7KSYvWm4pC03HlBAZ-ZEA"

app = Flask(__name__)

@app.route('/')
def alive():
    return "✅ Borrachinho_Bot está vivo."

# Telegram bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Olá Munir. Eu sou a tua Borrachinho_Bot. Sempre pronta para ti.")

async def lembrete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🕒 Lembrete registado!")

def run_bot():
    app_telegram = ApplicationBuilder().token(TOKEN).build()
    app_telegram.add_handler(CommandHandler("start", start))
    app_telegram.add_handler(CommandHandler("lembrete", lembrete))
    app_telegram.run_polling()

def run_web():
    app.run(host="0.0.0.0", port=10000)

if __name__ == '__main__':
    Thread(target=run_bot).start()
    Thread(target=run_web).start()
