import logging
import os
import sys
import warnings
import datetime as datetime

now = datetime.datetime.now()
dtftime = now.strftime("%Y_%m_%d")


log_filename = 'all_logs'+dtftime+'.log'

def appLogger():
    logger = logging.getLogger("predictivelogger")
    logger.setLevel(logging.INFO)

    fileHandler = logging.FileHandler(log_filename,mode='w')
    formater = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s",datefmt="%d/%m/%Y %I:%M:%S %p")

    fileHandler.setFormatter(formater)
    logger.addHandler(fileHandler)