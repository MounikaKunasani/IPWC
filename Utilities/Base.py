import pytest
import logging


@pytest.mark.usefixtures("setup")
class Base:

    def logging(self):
        logger = logging.getLogger(__name__)

        fileHandler = logging.FileHandler("Logs1.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        if logger.hasHandlers():
            logger.handlers.clear()
        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)

        return logger

