import logging


def set_logger():
    logging.basicConfig(
        format='%(levelname)s:%(funcName)s:%(asctime)s:%(message)s')


def get_logger(name):
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)
    return log
