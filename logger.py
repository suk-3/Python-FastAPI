import logging
import os

logfile = "logs/event.log"
consoleLogging = 1
fileLogging = 1


def putlog(name=__file__, loglevel=logging.DEBUG):
    """
    The `putlog` function sets up logging configuration with options for console and file logging.
    
    :param name: The `name` parameter in the `putlog` function is used to specify the name of the
    logger. By default, it is set to `__file__`, which represents the name of the current Python script
    file. You can provide a custom name for the logger by passing a string value to
    :param loglevel: The `loglevel` parameter in the `putlog` function determines the level of severity
    for logging messages. It specifies the minimum level of messages that will be logged. There are
    several log levels available in the Python `logging` module, including:
    :return: The function `putlog` is returning a logger object that has been configured with the
    specified log level and handlers for console and file logging.
    """
    os.makedirs(os.path.dirname(logfile), exist_ok=True)

    # logger
    logger = logging.getLogger(os.path.basename(name))
    logger.setLevel(loglevel)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s:%(lineno)d - %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')

    if consoleLogging == 1:
        ch = logging.StreamHandler()
        ch.setLevel(loglevel)
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    if fileLogging == 1:
        fh = logging.FileHandler(logfile)
        fh.setLevel(loglevel)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger