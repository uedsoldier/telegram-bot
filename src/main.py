from telegram_bot.telegram_bot import TelegramBot

print('Starting Telegram bot...')
bot = TelegramBot()
print('Polling bot...')
bot.app.run_polling(poll_interval=3)