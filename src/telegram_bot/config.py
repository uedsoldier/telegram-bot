import os 
from typing import Final

REDIS_HOST: Final = os.getenv('REDIS_HOST','localhost')
REDIS_CONTAINER_PORT: Final = int(os.getenv('REDIS_CONTAINER_PORT','6379'))
REDIS_ADMIN_USER: Final = os.getenv('REDIS_ADMIN_USER', 'default')
REDIS_ADMIN_PASSWORD: Final = os.getenv('REDIS_ADMIN_PASSWORD', None)

TELEGRAM_BOT_TOKEN: Final = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_ADMIN_ID: Final = int(os.getenv("TELEGRAM_ADMIN_ID"))
TELEGRAM_USER_ID: Final = os.getenv("TELEGRAM_USER_ID")

TELEGRAM_BOT_LOGFILE: Final = os.getenv('TELEGRAM_BOT_LOGFILE')