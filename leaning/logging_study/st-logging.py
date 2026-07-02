import logging

print("This is a print log")

logging.basicConfig(format='%(asctime)s | %(message)s | %(filename)s : %(lineno)s | %(levelname)s',
                    datefmt="%Y-%m-%d %H-%M-%S", level=logging.DEBUG)

logging.debug("This is a debug test")
logging.info("This is a info test")
logging.warning("This is a warning test")
logging.error("This is a error test")
logging.critical("This is a critical test")

# 记录器
logger = logging.getLogger()
logger.setLevel(logging.INFO)
# 处理器
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler(filename='addDemo.log', mode='a')
# 格式
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)


flt = logging.Filter("name")

fileHandler.addFilter(flt)
