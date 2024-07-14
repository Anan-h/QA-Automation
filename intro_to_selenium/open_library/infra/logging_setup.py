import logging


class LoggingSetup:
    logging.basicConfig(filename="../open_library.log",
                        level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s ',
                        force=True)
