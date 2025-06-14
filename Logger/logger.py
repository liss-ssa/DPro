import logging
from time import asctime

FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(filename='Logger/processing_logs.log', level=logging.INFO, format=FORMAT)
logger = logging.getLogger(__name__)


def decorator(func):
    message_1 = f'{func.__name__} started.'
    message_2 = f'{func} finished.'
    def wrapper(*args):
        logging.info(message_1)
        result = func(*args)
        logging.info(message_2)
        return result
    return wrapper