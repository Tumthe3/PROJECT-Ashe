# -*- coding: utf-8 -*-
import logging
import logging.config
from bot import Bot

logging.config.fileConfig("logging.ini")
logger = logging.getLogger("main")

def main():
    FILE_CONFIG = "settings.ini"
    ashe = Bot(FILE_CONFIG)
    ashe.run()


if "__main__" == __name__:
    main()
