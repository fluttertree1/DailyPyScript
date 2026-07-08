# ------------------------第三方库--------------------------
from datetime import datetime, timedelta
import logging
# ----------------------引用自定义函数-----------------------
from QiKe import QiKe_TianPan
from switchHour import switchtime
from QiKe import JiGong
from QiKe import QiSiKe
# -----------------------配置logging-----------------------
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
    def Sheng(self, element):
        if element == '巳' or element == '午':
            return 1
    def Ke(self, element):
        if element == '辰' or element == '戌' or element == '丑' or element == '未':
            return -1
    def Tong(self, element):
        if element == '寅' or element == '卯':
            return 0



class Fire:
    def __init__(self, name):
        self.name = name

    def Sheng(self, element):
        if element == '辰' or element == '戌' or element == '丑' or element == '未':
            return 1

    def Ke(self, element):
        if element == '申' or element == '酉':
            return -1

    def Tong(self, element):
        if element == '巳' or element == '午':
            return 0


class Soil:
    def __init__(self, name):
        self.name = name

    def Sheng(self, element):
        if element == '申' or element == '酉':
            return 1

    def Ke(self, element):
        if element == '亥' or element == '子':
            return -1

    def Tong(self, element):
        if element == '辰' or element == '戌' or element == '丑' or element == '未':
            return 0


class Metal:
    def __init__(self, name):
        self.name = name

    def Sheng(self, element):
        if element == '亥' or element == '子':
            return 1

    def Ke(self, element):
        if element == '寅' or element == '卯':
            return -1

    def Tong(self, element):
        if element == '申' or element == '酉':
            return 0


class Water:
    def __init__(self, name):
        self.name = name

    def Sheng(self, element):
        if element == '寅' or element == '卯':
            return 1

    def Ke(self, element):
        if element == '巳' or element == '午':
            return -1

    def Tong(self, element):
        if element == '亥' or element == '子':
            return 0


class YangWood(Yang, Wood):
    def __init__(self, name):
        self.name = name


class YinWood(Yin, Wood):
    def __init__(self, name):
        self.name = name


class YangFire(Yang, Fire):
    def __init__(self, name):
        self.name = name


class YinFire(Yin, Fire):
    def __init__(self, name):
        self.name = name


class YangSoil(Yang, Soil):
    def __init__(self, name):
        self.name = name


class YinSoil(Yin, Soil):
    def __init__(self, name):
        self.name = name


class YangMetal(Yang, Metal):
    def __init__(self, name):
        self.name = name


class YinMetal(Yin, Metal):
    def __init__(self, name):
        self.name = name


class YangWater(Yang, Water):
    def __init__(self, name):
        self.name = name


class YinWater(Yin, Water):
    def __init__(self, name):
        self.name = name


Yang_lwood = YangWood("寅")  # l = land 地支
Yin_lwood = YinWood("卯")
Yang_lfire = YangFire("巳")
Yin_lfire = YinFire("午")
Yang_lsoilChen = YangSoil("辰")
Yang_lsoilXu = YangSoil("戌")
Yin_lsoilChou = YangSoil("丑")
Yin_lsoilWei = YangSoil("未")
Yang_lmetal = YangMetal("申")
Yin_lmetal = YinMetal("酉")
Yang_lwater = YangWater("子")
Yin_lwater = YinWater("亥")

classDict = {
    "寅": Yang_lwood, "卯": Yin_lwood,
    "巳": Yang_lfire, "午": Yin_lfire,
    "辰": Yang_lsoilChen, "戌": Yang_lsoilXu,
    "丑": Yin_lsoilChou, "未": Yin_lsoilWei,
    "申": Yang_lmetal, "酉": Yin_lmetal,
    "子": Yang_lwater, "亥": Yin_lwater
}


day = "壬辰"
TianPan = QiKe_TianPan("清明", '丁卯')
print(TianPan)
QiSiKe(day, TianPan)

# 贼克法
def JiuZongMen():
    SiKe = QiSiKe(day, TianPan)
    GanJi = JiGong(SiKe[1][3])
    # 判断四课中有没有贼
    if classDict[GanJi].Ke(SiKe[0][3]) == -1 or classDict[SiKe[1][2]].Ke(SiKe[0][2]) == -1 or classDict[SiKe[1][1]].Ke(SiKe[0][1] == -1 or classDict[[1][0]].Ke(SiKe[0][0]) == -1:



# 比用法
# 涉害法
# 蒿失法
# 昴星法
# 别责法
# 八专法
# 伏吟法
# 反吟法