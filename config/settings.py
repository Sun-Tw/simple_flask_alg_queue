import os

# alg process queue
from multiprocessing import Queue
alg_queue = Queue(100)


# logging
import logging
import logging.handlers


def init_logger():
    if not os.path.isdir("logs"):
        os.makedirs("logs")
    logger = logging.getLogger("flask")
    logger.setLevel(logging.INFO)
    log_file_size = 1024 * 1024 * 100
    log_backup_num = 5
    fh = logging.handlers.RotatingFileHandler("logs/flask.log",maxBytes=log_file_size,backupCount=log_backup_num)
    formatter = logging.Formatter("[%(asctime)s] - %(pathname)s:%(lineno)s - %(message)s")
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger

logger = init_logger()


# set uplpad video path
video_save_path = "media/uploads"
if not os.path.isdir(video_save_path):
    os.makedirs(video_save_path)

