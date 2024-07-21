import logging


class Logger:
    logging.basicConfig(filename="../api_imdb.log",
                        level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s ',
                        force=True)
