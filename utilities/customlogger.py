import logging
import logging.config
import inspect

class customlogger:

    def customlogg(self, loglevel=logging.DEBUG):

        loggername = inspect.stack()[1][3]

        logger = logging.getLogger(loggername)
        logger.setLevel(logging.INFO)

        filehandler = logging.FileHandler("automation.log", mode='a')
        #filehandler = logging.StreamHandler()
        filehandler.setLevel(loglevel)

        formatter = logging.Formatter("%(asctime)s:- %(name)s- %(levelname)s: %(message)s", datefmt="%d-%m-%y %H:%M:%S")

        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        return logger

