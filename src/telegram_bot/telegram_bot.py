from telegram.ext import ApplicationBuilder, Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import Update
from telegram_bot.config import TELEGRAM_BOT_TOKEN, TELEGRAM_USER_ID
from telegram_bot.redis_store import RedisStore

class TelegramBot:
    def __init__(self, token: str = TELEGRAM_BOT_TOKEN):
        print(f'Token: {token}')
        self.store = RedisStore()
        self.token = token
        self.key_forced_phrases = 'forced_phrases'
        self.app : Application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
        self._register_handlers()

    def _register_handlers(self):
        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(CommandHandler("help", self.help))
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.message_handler))
        self.app.add_error_handler(self.error_handler)
    
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text('Bienvenido al bot. Usa /add para añadir frases forzadas.')
    
    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text('Texto de ayuda')
    
    async def message_handler(self,update: Update, context: ContextTypes.DEFAULT_TYPE):
        message_type: str = update.message.chat.type
        text: str = update.message.text

        print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

        if message_type == 'group':
            if TELEGRAM_USER_ID in text:
                new_text: str = text.replace(TELEGRAM_USER_ID, '').strip()
                response: str = self.response_handler(new_text)
            else:
                return
        else: 
            response: str = self.response_handler(text)
        print('Bot: '+response)
        await  update.message.reply_text(response)
    
    def response_handler(self, text: str) -> str:
        processed_text: str = text.lower()
        if 'hola' in processed_text:
            return 'mundo'
        return 'No entiendo'
    
    async def error_handler(self,update: Update, context: ContextTypes.DEFAULT_TYPE):
        print(f'Update {update} caused error {context.error}')
        
