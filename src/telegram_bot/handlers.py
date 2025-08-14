from telegram import Update
from telegram.ext import ContextTypes

class TelegramBotHandlers:
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text('Bienvenido al bot. Usa /add para añadir frases forzadas.')
    
    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text('Texto de ayuda')
