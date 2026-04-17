import logging
import os
from datetime import datetime
from config.settings import LOG_DIR

def get_logger():
    logger = logging.getLogger("auto_test")
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    if not os.path.exists(LOG_DIR):
        os.mkdir(LOG_DIR)

    log_file = os.path.join(LOG_DIR, f"{datetime.now().strftime('%Y%m%d')}.log")
    fh = logging.FileHandler(log_file, encoding="utf-8")
    ch = logging.StreamHandler()

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger

logger = get_logger()