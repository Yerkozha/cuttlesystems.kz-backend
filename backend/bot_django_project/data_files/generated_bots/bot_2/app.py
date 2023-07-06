import sys
import logging.handlers
from loader import dp
from aiogram import executor
from handlers import dp
from on_startup_commands import set_default_commands

logger_format = '%(asctime)s - %(name)s:%(lineno)s - %(levelname)s - %(message)s'
rotating_file_handler = logging.handlers.RotatingFileHandler(
    filename='C:\\www\\cuttlesystem-backend\\tg_bot_constructor\\backend\\bot_django_project\\data_files\\generated_bots\\bot_logs\\bot_2.log',
    mode='a',
    maxBytes=5000000,
    backupCount=5
)
stream_handler = logging.StreamHandler(stream=sys.stdout)
logging.basicConfig(level=logging.INFO, format=logger_format, handlers=[rotating_file_handler, stream_handler])

if __name__ == '__main__':
    logging.info('Bot started')
    sys.stdout.flush()
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=set_default_commands)
