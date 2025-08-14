
import os, sys
from telegram_bot.log_manager import LogManager

HEALTHCHECK_STR = '[TelegramHealthCheck]'
logger = LogManager.get_logger(__name__)


def check_env():
    # Variables que deben estar presentes
    required_vars = [
        'TELEGRAM_BOT_TOKEN',
        'REDIS_HOST',
        'REDIS_CONTAINER_PORT',
        'REDIS_ADMIN_USER',
        'REDIS_ADMIN_PASSWORD'
    ]

    missing = []

    logger.info(f'{HEALTHCHECK_STR} Verifying environment variables...')

    for var in required_vars:
        if not os.getenv(var):
            missing.append(var)
    if missing:
        logger.error(f'{HEALTHCHECK_STR} ERROR: Critical variables are missing: {", ".join(missing)}')
        sys.exit(1)
    else:
        logger.info(f'{HEALTHCHECK_STR} All required variables are loaded.')

def check_redis():
    logger.info(f'{HEALTHCHECK_STR} Checking Redis connection...')
    try:
        redis_store = RedisStore()
        if redis_store.ping():
            logger.info(f'{HEALTHCHECK_STR} ✅ Redis PING successful.')
        else:
            logger.error(f'{HEALTHCHECK_STR} ❌ Redis PING failed.')
            sys.exit(1)
       
    except Exception as e:
        logger.error(f'{HEALTHCHECK_STR} ❌ Error connecting to Redis: {e}.')
        sys.exit(1)
    logger.info(f'{HEALTHCHECK_STR} ✅ Redis connection is healthy.')

def check_twitter():
    logger.info(f'{HEALTHCHECK_STR} Checking Twitter API connection...')
    try:
        twitter_client = TwitterClient(
            TWITTER_ACCESS_TOKEN=os.getenv('TWITTER_ACCESS_TOKEN'),
            TWITTER_ACCESS_TOKEN_SECRET=os.getenv('TWITTER_ACCESS_TOKEN_SECRET'),
            TWITTER_CONSUMER_KEY=os.getenv('TWITTER_CONSUMER_KEY'),
            TWITTER_CONSUMER_SECRET=os.getenv('TWITTER_CONSUMER_SECRET')
        )
        response: UserResponse = twitter_client.get_me()
        if response.success:
            logger.info(f'{HEALTHCHECK_STR} User info retrieved successfully: {response.user_data}')
        else:
            logger.error(f'{HEALTHCHECK_STR} ❌ Error getting user info: {response.error} (Status code: {response.status_code})')
            sys.exit(1)

        logger.info(f'{HEALTHCHECK_STR} ✅ Twitter API connection is healthy.')
    except Exception as e:
        logger.error(f'{HEALTHCHECK_STR} ❌ Error connecting to Twitter API: {e}.')
        sys.exit(1)

if __name__ == '__main__':
    check_env()
    check_redis()
    check_twitter()
    sys.exit(0)