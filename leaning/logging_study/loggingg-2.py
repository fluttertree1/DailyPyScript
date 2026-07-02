import logging
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
