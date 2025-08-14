import logging
import sys
from telegram_bot.config import TELEGRAM_BOT_LOGFILE

class LogManager:
    @staticmethod
    def get_logger(name: str = 'telegram_bot', level: int = logging.INFO, to_file=False, file_path=TELEGRAM_BOT_LOGFILE) -> logging.Logger:
        logger = logging.getLogger(name)
        if logger.hasHandlers():
            return logger
        
        logger.setLevel(level)

        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')

        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        if to_file:
            file_handler = logging.FileHandler(file_path)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        
        return logger