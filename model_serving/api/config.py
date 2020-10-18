import logging
from logging.handlers import TimedRotatingFileHandler
import pathlib
import os
import sys
from pydantic import BaseConfig,BaseModel

PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent.parent

FORMATTER = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s —"
    "%(funcName)s:%(lineno)d — %(message)s")
LOG_DIR = PACKAGE_ROOT / 'logs'
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / 'ml_api.log'


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler():
    file_handler = TimedRotatingFileHandler(
        LOG_FILE, when='midnight')
    file_handler.setFormatter(FORMATTER)
    file_handler.setLevel(logging.WARNING)
    return file_handler


def get_logger(*, logger_name):
    """Get logger with prepared handlers."""

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    logger.propagate = False

    return logger


class Config(BaseModel):
    debug = False
    port=3000
 


class ProductionConfig(Config):
    debug = False
    port = os.environ.get('PORT', 5000)
    host="0.0.0.0"


class DevelopmentConfig(Config):
    debug = True
    port=5000
    host = "0.0.0.0"
    #host="172.17.0.2" #for docker 
    
