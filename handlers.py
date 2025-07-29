from telegram import Update
from telegram.ext import ContextTypes

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! O Borrachinho_Bot está ativo e pronto para te ajudar!")

async def comando_rotina(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Comando /rotina recebido.")

async def comando_entrada(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Comando /entrada recebido.")

async def comando_resumo_financeiro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Aqui está o teu resumo financeiro!")