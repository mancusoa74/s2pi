"""
Created on July 26 2017

@author: Antonio Mancuso

@version: 0.1 - July 2017

This is a simple logging facility which implements Time Rotation and Colored log
"""

import logging
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

global logger

def init(level):
	"""
	Initialize the logger
	:param Level: the initial logging Level
        :return: None
	"""
	global logger

	try:
		logHandler = TimedRotatingFileHandler("s2pi.log",when="D", interval=1)
		formatter = ColoredFormatter(
			"%(asctime)s - %(log_color)s%(levelname)-8s - %(white)s%(message)s",
			datefmt=' %d-%m-%Y %H:%M:%S',
			reset=True,
			log_colors={
			    'DEBUG':    'cyan',
			    'INFO':     'green',
			    'WARNING':  'yellow',
			    'ERROR':    'red',
			    'CRITICAL': 'red',
			}
		)

		logHandler.setFormatter(formatter)
		logger = logging.getLogger('s2rpi')
		logger.addHandler(logHandler)
		logger.setLevel(level)
	except: 
		print("Error initializing logging...Cannot continue")
		raise SystemExit

def debug(message):
    logger.debug(message)

def info(message):
    logger.info(message)

def warning(message):
    logger.warning(message)

def error(message):
    logger.error(message)

def critical(message):
    logger.critical(message)
