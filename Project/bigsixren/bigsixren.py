from datetime import datetime, timedelta
import logging
from QiKe import QiKe_TianPan
from switchHour import switchtime
# -----------------------配置logging------------------------
# 记录器
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# 处理器
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler(filename='liurenDemo.log', mode='a', encoding='utf-8')
fileHandler.setLevel(logging.DEBUG)
# 格式
formatter = logging.Formatter("%(asctime)s | %(levelname)-8s | %(lineno)d | %(message)10s |")

consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

# -----------------------------------------------------------

# 定义阴阳五行对象

TIANGAN = "甲乙丙丁戊己庚辛壬癸"  # 0-9
DIZHI = "子丑寅卯辰巳午未申酉戌亥"  # 0-11
JIEQI = {  # 节气与月将对应表(简化版)
    '立春': '寅', '雨水': '卯', '惊蛰': '辰', '春分': '巳',
    '清明': '午', '谷雨': '未', '立夏': '申', '小满': '酉',
    '芒种': '戌', '夏至': '亥', '小暑': '子', '大暑': '丑'
}

# 主体架构
# def liuren_qiuke(date, hour):
#     """大六壬起课主函数"""
#     # 输入处理
#     lunar_month = get_jieqi(date)  # 获取节气函数
#     hour_dizhi = hour_to_dizhi(hour)  # 时辰转地支
#
#     # 构建天地盘
#     terrestrial, celestial = build_celestial_map(lunar_month, hour_dizhi)
#
#     # 生成四课
#     sike = generate_sike(date.tiangan, date.dizhi, celestial, terrestrial)
#
#     # 九宗门发三传
#     sanchuan = jiuzongmen(sike, date.tiangan)

# 转换时间

class Yin:
    def __init__(self):
        self.property = 0


class Yang:
    def __init__(self):
        self.property = 1


class Wood:
    def __init__(self, name):
        self.name = name
    
    def beneficial_(self):
        print("火生土")

    def harm_(self):
        print("木克土")


class Fire:
    def __init__(self, name):
        self.name = name

    def beneficial_(self):
        print("火生土")

    def harm_(self):
        print("火克金")


class Soil:
    def __init__(self, name):
        self.name = name

    def beneficial_(self):
        print("土生金")

    def harm_(self):
        print("土克水")


class Metal:
    def __init__(self, name):
        self.name = name

    def beneficial_(self):
        print("金生水")

    def harm_(self):
        print("金克木")


class Water:
    def __init__(self, name):
        self.name = name

    def beneficial_(self):
        print("水生木")

    def harm_(self):
        print("水克火")


class YangWood(Yang, Wood):
    def __init__(self, name):
        self.name = name


class YinWood(Yin, Wood):
    def __init__(self, name):
        super().__init__(name)


class YangFire(Yang, Fire):
    def __init__(self, name):
        super().__init__(name)


class YinFire(Yin, Fire):
    def __init__(self, name):
        super().__init__(name)


class YangSoil(Yang, Soil):
    def __init__(self, name):
        super().__init__(name)


class YinSoil(Yin, Soil):
    def __init__(self, name):
        super().__init__(name)


class YangMetal(Yang, Metal):
    def __init__(self, name):
        super().__init__(name)


class YinMetal(Yin, Metal):
    def __init__(self, name):
        super().__init__(name)


class YangWater(Yang, Water):
    def __init__(self, name):
        super().__init__(name)


class YinWater(Yin, Water):
    def __init__(self, name):
        super().__init__(name)


Yang_swood = YangWood("甲")  # s = sky 天干
# Yin_swood = YinWood("乙")
# Yang_lwood = YangWood("寅")  # l = land 地支
# Yin_lwood = YinWood("卯")
# Yang_sfire = YangFire("丙")
# Yin_sfire = YinFire("丁")
# Yang_ssoil = YangSoil("戊")
# Yin_lsoil = YinSoil("己")
# Yang_lsoilChen = YangSoil("辰")
# Yang_lsoilXu = YangSoil("戌")
# Yang_lsoilChou = YangSoil("丑")
# Yang_lsoilWei = YangSoil("未")
print(Yang_swood.name)


if __name__ == '__main__':
    try:
        # now = datetime.now()
        # print(f"当前日期和时间: {now.hour}")
        # year = int(input("请输入年份；"))
        # month = int(input("请输入月份："))
        # day = int(input("请输入日期："))
        hour = int(input("请输入时间："))
        minute = int(input("请输入分钟："))
        HourZhi = switchtime(hour, minute)

    except Exception as e:
        logger.debug(f"请输入数字{e}")


# 贼克法

# 比用法
# 涉害法
# 蒿失法
# 昴星法
# 别责法
# 八专法
# 伏吟法
# 反吟法