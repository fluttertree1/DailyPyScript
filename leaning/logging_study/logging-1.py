import logging

print("This is a print log")

logging.basicConfig(format='%(asctime)s | %(message)s | %(filename)s : %(lineno)s | %(levelname)s',
                    datefmt="%Y-%m-%d %H-%M-%S", level=logging.DEBUG)

logging.debug("This is a debug test")
logging.info("This is a info test")
logging.warning("This is a warning test")
logging.error("This is a error test")
logging.critical("This is a critical test")
