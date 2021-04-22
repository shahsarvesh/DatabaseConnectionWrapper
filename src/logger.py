import logging
import sys
# from logging.handlers import TimedRotatingFileHandler

console_formatter = logging.Formatter("%(asctime)s %(filename)s: %(funcName)s: %(lineno)s %(levelname)s: %(message)s", "%Y-%m-%d %H:%M:%S")
file_formatter = logging.Formatter("""{"time": "%(asctime)s","file_name": "%(filename)s", "function_name": "%(funcName)s", "line_no": "%(lineno)s", "level" : "%(levelname)s", "message": "%(message)s"}""", "%Y-%m-%d %H:%M:%S")


def get_console_handler():
   console_handler = logging.StreamHandler(sys.stdout)
   console_handler.setFormatter(console_formatter)
   return console_handler
   
def get_file_handler(log_file_name):
   file_handler = logging.FileHandler(log_file_name)
   file_handler.setFormatter(file_formatter)
   return file_handler

def get_logger(logger_name, log_file_name):
   logger = logging.getLogger(logger_name)
   logger.setLevel(logging.DEBUG) 
   logger.addHandler(get_console_handler())
   logger.addHandler(get_file_handler(log_file_name))

   logger.propagate = False
   return logger   