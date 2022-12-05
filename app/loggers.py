import logging


def get_inside_logger():
    """
    Used for inside detect events only
    """
    logger = logging.getLogger('tile38_ins')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
    if not logger.hasHandlers():
        file_handler = logging.FileHandler('logs/inside-events.log')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger

def get_misc_events_logger():
    """
    Used to log events:
        cross
        enter
        exit
        outside
    """
    logger = logging.getLogger('tile38_cee')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
    if not logger.hasHandlers():
        file_handler = logging.FileHandler('logs/misc-events.log')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger