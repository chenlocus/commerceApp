import logging

class LogGen:

    @staticmethod
    def loggen():
        # logging.basicConfig(format='%(asctime)s %(message)s',
        #                     datefmt='%m/%d/%Y %I:%M:%S %p')
        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
        logger = logging.getLogger()
        handler = logging.FileHandler('.\\Logs\\automation.log')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger
