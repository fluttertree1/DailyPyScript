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
SIXTYJIAZI = ["甲子", "乙丑", "丙寅", "丁卯", "戊辰", "己巳", "庚午", "辛未", "壬申", "癸酉",
               "甲戌", "乙亥", "丙子", "丁丑", "戊寅", "己卯", "庚辰", "辛巳", "壬午", "癸未",
               "甲申", "乙酉", "丙戌", "丁亥", "戊子", "己丑", "庚寅", "辛卯", "壬辰", "癸巳",
               "甲午", "乙未", "丙申", "丁酉", "戊戌", "己亥", "庚子", "辛丑", "壬寅", "癸卯",
               "甲辰", "乙巳", "丙午", "丁未", "戊申", "己酉", "庚戌", "辛亥", "壬子", "癸丑",
               "甲寅", "乙卯", "丙辰", "丁巳", "戊午", "己未", "庚申", "辛酉", "壬戌", "癸亥"]



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
        if element == '巳' or element == '午' or element == '丙' or element == '丁':
            return 1
    def Ke(self, element):
        if element == '辰' or element == '戌' or element == '丑' or element == '未' or element == '戊' or element == '己':
            return -1
    def Tong(self, element):
        if element == '寅' or element == '卯' or element == '甲' or element == '乙':
            return 0
    def BKe(self, element):
        if element == '申' or element == '酉' or element == '庚' or element == '辛':
            return -2
    def BSheng(self, element):
        if element == '子' or element == '亥' or element == '壬' or element == '癸':
            return 2



class Fire:
    def __init__(self, name):
        self.name = name

    def Sheng(self, element):
        if element == '辰' or element == '戌' or element == '丑' or element == '未' or element == '戊' or element == '己':
            return 1

    def Ke(self, element):
        if element == '申' or element == '酉' or element == '庚' or element == '辛':
            return -1

    def Tong(self, element):
        if element == '巳' or element == '午' or element == '丙' or element == '丁':
            return 0
    def BKe(self, element):
        if element == '子' or element == '亥' or element == '壬' or element == '癸':
            return -2
    def BSheng(self, element):
        if element == '寅' or element == '卯' or element == '甲' or element == '乙':
            return 2

class Soil:
    def __init__(self, name):
        self.name = name

    def Sheng(self, element):
        if element == '申' or element == '酉' or element == '庚' or element == '辛':
            return 1

    def Ke(self, element):
        if element == '子' or element == '亥' or element == '壬' or element == '癸':
            return -1

    def Tong(self, element):
        if element == '辰' or element == '戌' or element == '丑' or element == '未' or element == '戊' or element == '己':
            return 0
    def BKe(self, element):
        if element == '寅' or element == '卯' or element == '甲' or element == '乙':
            return -2
    def BSheng(self, element):
        if element == '巳' or element == '午' or element == '丙' or element == '丁':
            return 2

class Metal:
    def __init__(self, name):
        self.name = name

    def Sheng(self, element):
        if element == '子' or element == '亥' or element == '壬' or element == '癸':
            return 1

    def Ke(self, element):
        if element == '寅' or element == '卯' or element == '甲' or element == '乙':
            return -1

    def Tong(self, element):
        if element == '申' or element == '酉' or element == '庚' or element == '辛':
            return 0
    def BKe(self, element):
        if element == '巳' or element == '午' or element == '丙' or element == '丁':
            return -2
    def BSheng(self, element):
        if element == '辰' or element == '戌' or element == '丑' or element == '未' or element == '戊' or element == '己':
            return 2

class Water:
    def __init__(self, name):
        self.name = name

    def Sheng(self, element):
        if element == '寅' or element == '卯' or element == '甲' or element == '乙':
            return 1

    def Ke(self, element):
        if element == '巳' or element == '午' or element == '丙' or element == '丁':
            return -1

    def Tong(self, element):
        if element == '子' or element == '亥' or element == '壬' or element == '癸':
            return 0
    def BKe(self, element):
        if element == '辰' or element == '戌' or element == '丑' or element == '未' or element == '戊' or element == '己':
            return -2
    def BSheng(self, element):
        if element == '申' or element == '酉' or element == '庚' or element == '辛':
            return 2

class YangWood(Yang, Wood):
    def __init__(self, name):
        self.name = name
        super().__init__()

class YinWood(Yin, Wood):
    def __init__(self, name):
        self.name = name
        super().__init__()

class YangFire(Yang, Fire):
    def __init__(self, name):
        self.name = name
        super().__init__()

class YinFire(Yin, Fire):
    def __init__(self, name):
        self.name = name
        super().__init__()

class YangSoil(Yang, Soil):
    def __init__(self, name):
        self.name = name
        super().__init__()

class YinSoil(Yin, Soil):
    def __init__(self, name):
        self.name = name
        super().__init__()

class YangMetal(Yang, Metal):
    def __init__(self, name):
        self.name = name
        super().__init__()

class YinMetal(Yin, Metal):
    def __init__(self, name):
        self.name = name
        super().__init__()

class YangWater(Yang, Water):
    def __init__(self, name):
        self.name = name
        super().__init__()

class YinWater(Yin, Water):
    def __init__(self, name):
        self.name = name
        super().__init__()


Yang_swood = YangWood("甲")  #s = sky 天干
Yin_swood = YinWood("乙")
Yang_lwood = YangWood("寅")  # l = land 地支
Yin_lwood = YinWood("卯")

Yang_sfire = YangFire("丙")
Yin_sfire = YinFire("丁")
Yang_lfire = YangFire("午")
Yin_lfire = YinFire("巳")

Yang_ssoil = YangSoil("戊")
Yin_ssoil = YinSoil("己")
Yang_lsoilChen = YangSoil("辰")
Yang_lsoilXu = YangSoil("戌")
Yin_lsoilChou = YinSoil("丑")
Yin_lsoilWei = YinSoil("未")

Yang_smetal = YangMetal("庚")
Yin_smetal = YinMetal("辛")
Yang_lmetal = YangMetal("申")
Yin_lmetal = YinMetal("酉")

Yang_swater = YangWater("壬")
Yin_swater = YinWater("癸")
Yang_lwater = YangWater("子")
Yin_lwater = YinWater("亥")

classDict = {
    "寅": Yang_lwood, "卯": Yin_lwood,
    "午": Yang_lfire, "巳": Yin_lfire,
    "辰": Yang_lsoilChen, "戌": Yang_lsoilXu,
    "丑": Yin_lsoilChou, "未": Yin_lsoilWei,
    "申": Yang_lmetal, "酉": Yin_lmetal,
    "子": Yang_lwater, "亥": Yin_lwater
}

JigongDict = {
    "丑": Yin_swater, "辰": Yin_swood,
    "未": [Yin_sfire, Yin_ssoil], "戌": Yin_smetal,
    "寅": Yang_swood, "申": Yang_smetal,
    "巳": [Yang_sfire, Yang_ssoil], "亥": Yang_swater
}


def SanChuanindex(Chu):
    ZhongIdx = DIZHI.index(Chu)
    Zhong = TianPan[ZhongIdx]
    MuoIdx = DIZHI.index(Zhong)
    Muo = TianPan[MuoIdx]
    return [Chu, Zhong, Muo]


def SheHuiBenJia(ShangShen, choice):  # 涉回本家  ShangShen 为 list
    # 如果都是下克上（贼）
    if choice == 0:  # 0 代表下（阴）克上
        biyong_ls = []
        for shen in ShangShen:  # 对每个上神进行统计
            Bke_count = 0
            ShenIdx = TianPan.index(shen)
            ShenUnder = DIZHI[ShenIdx]
            shenidx = DIZHI.index(shen)
            if ShenIdx < shenidx:  # 天盘位置比地盘位置靠后
                for dizhi in DIZHI[ShenIdx:shenidx+1:]:  # 对地盘检查寄宫
                    Jigong_condition = [dizhi == '丑', dizhi == '辰', dizhi == '戌', dizhi == '寅', dizhi == '申', dizhi == '亥']
                    Jigong_conditionDouble = [dizhi == '未', dizhi == '巳']
                    if any(Jigong_condition):
                        if classDict[shen].BKe(JigongDict[dizhi].name) == -2:
                            Bke_count += 1
                    if any(Jigong_conditionDouble):
                        for jigan in JigongDict[dizhi]:
                            if classDict[shen].BKe(jigan.name) == -2:
                                Bke_count += 1
                    if classDict[shen].BKe(dizhi) == -2:
                        Bke_count += 1
                # 统计完后再添加
                biyong_ls.append(Bke_count)
            if ShenIdx > shenidx:  # 天盘位置比地盘靠前
                diff = 11 - ShenIdx - shenidx
                New_DIZHI = DIZHI[shenidx+1::] + DIZHI[:shenidx+1:]  # 转换到前面
                new_shenidx = New_DIZHI.index(shen)
                New_ShenUnderIdx = New_DIZHI.index(ShenUnder)
                for dizhi in New_DIZHI[New_ShenUnderIdx:new_shenidx+1:]:
                    Jigong_condition = [dizhi == '丑', dizhi == '辰', dizhi == '戌', dizhi == '寅', dizhi == '申',
                                        dizhi == '亥']
                    Jigong_conditionDouble = [dizhi == '未', dizhi == '巳']
                    if any(Jigong_condition):
                        if classDict[shen].BKe(JigongDict[dizhi].name) == -2:  # JigongDict[dizhi]返回的是一个地址
                            Bke_count += 1
                    if any(Jigong_conditionDouble):
                        for jigan in JigongDict[dizhi]:
                            if classDict[shen].BKe(jigan.name) == -2:
                                Bke_count += 1
                    if classDict[shen].BKe(dizhi) == -2:
                        Bke_count += 1
                biyong_ls.append(Bke_count)
        biyongShangshen = zip(biyong_ls, ShangShen)
        max_value = max(biyong_ls)
        all_max = [item for item in biyongShangshen if item[0] == max_value]
        for value, name in all_max:
            if value == max_value:
                Chu = name
                return SanChuanindex(Chu)

    # 如果都是上克下
    if choice == 1:
        biyong_ls = []
        for shen in ShangShen:  # 对每个上神进行统计
            ke_count = 0
            ShenIdx = TianPan.index(shen)
            ShenUnder = DIZHI[ShenIdx]
            shenidx = DIZHI.index(shen)
            if ShenIdx < shenidx:  # 天盘位置比地盘位置靠后
                for dizhi in DIZHI[ShenIdx:shenidx + 1:]:
                    Jigong_condition = [dizhi == '丑', dizhi == '辰', dizhi == '戌', dizhi == '寅', dizhi == '申',
                                        dizhi == '亥']
                    Jigong_conditionDouble = [dizhi == '未', dizhi == '巳']
                    if any(Jigong_condition):
                        if classDict[shen].Ke(JigongDict[dizhi]) == -1:
                            ke_count += 1
                    if any(Jigong_conditionDouble):
                        for jigan in JigongDict[dizhi]:
                            if classDict[shen].Ke(jigan.name) == -1:
                                ke_count += 1
                    if classDict[shen].Ke(dizhi) == -1:
                        ke_count += 1

                biyong_ls.append(ke_count)
            if ShenIdx > shenidx:  # 天盘位置比地盘靠前
                diff = 11 - ShenIdx - shenidx
                New_DIZHI = DIZHI[shenidx + 1::] + DIZHI[:shenidx + 1:]  # 转换到前面
                new_shenidx = New_DIZHI.index(shen)
                New_ShenUnderIdx = New_DIZHI.index(ShenUnder)
                for dizhi in New_DIZHI[New_ShenUnderIdx:new_shenidx + 1:]:
                    Jigong_condition = [dizhi == '丑', dizhi == '辰', dizhi == '戌', dizhi == '寅', dizhi == '申',
                                        dizhi == '亥']
                    Jigong_conditionDouble = [dizhi == '未', dizhi == '巳']
                    if any(Jigong_condition):
                        if classDict[shen].Ke(JigongDict[dizhi].name) == -1:
                            ke_count += 1
                    if any(Jigong_conditionDouble):
                        for jigan in JigongDict[dizhi]:
                            if classDict[shen].Ke(jigan.name) == -1:
                                ke_count += 1
                    if classDict[shen].Ke(dizhi) == -1:
                        ke_count += 1

                biyong_ls.append(ke_count)
        biyongShangshen = zip(biyong_ls, ShangShen)
        max_value = max(biyong_ls)
        all_max = [item for item in biyongShangshen if item[0] == max_value]
        for value, name in all_max:
            if value == max_value:
                Chu = name
                return SanChuanindex(Chu)


def ZeiKe():
    SiKe = QiSiKe(day, TianPan)
    GanJi = JiGong(SiKe[1][3])
    # 有贼克的情况
    # 判断四课中有没有贼
    conditions = [classDict[GanJi].Ke(SiKe[0][3]) == -1, classDict[SiKe[1][2]].Ke(SiKe[0][2]) == -1,
                  classDict[SiKe[1][1]].Ke(SiKe[0][1]) == -1, classDict[SiKe[1][0]].Ke(SiKe[0][0]) == -1]
    sikenames = ['一课', '二课', '三课', '四课']
    true_conditions = []  # 有贼的课
    true_count = sum(condition for condition in conditions)
    for condition, name in zip(conditions, sikenames):
        if condition:
            true_conditions.append(name)

    Kecondition = [classDict[SiKe[0][3]].Ke(GanJi) == -1, classDict[SiKe[0][2]].Ke(SiKe[1][2]) == -1,
                   classDict[SiKe[0][1]].Ke(SiKe[1][1]) == -1, classDict[SiKe[0][0]].Ke(SiKe[1][0]) == -1]
    true_kecondition = []  # 有克的课
    true_kecount = sum(condition for condition in Kecondition)
    for value, name in zip(Kecondition, sikenames):
        if value:
            true_kecondition.append(name)

    # 只有贼的情况
    if any(conditions) and not any(Kecondition):
        if true_count == 1:
            for name in sikenames:
                if true_conditions[0] == name:
                    if name == '一课':
                        Chu = SiKe[0][3]
                    elif name == '二课':
                        Chu = SiKe[0][2]
                    elif name == '三课':
                        Chu = SiKe[0][1]
                    elif name == '四课':
                        Chu = SiKe[0][0]
            return SanChuanindex(Chu)
        # 贼的个数为大于等于2时，使用比用法
        if true_count == 2:
            # zeiname 为四课中的天盘
            zeiname = []
            for true_condition_name in true_conditions:
                if true_condition_name == '一课':
                    zei = SiKe[0][3]
                    zeiname.append(zei)
                elif true_condition_name == '二课':
                    zei = SiKe[0][2]
                    zeiname.append(zei)
                elif true_condition_name == '三课':
                    zei = SiKe[0][1]
                    zeiname.append(zei)
                elif true_condition_name == '四课':
                    zei = SiKe[0][0]
                    zeiname.append(zei)
            # 第一个贼判断
            if classDict[zeiname[0]].property == classDict[GanJi].property and\
                    classDict[zeiname[1]].property != classDict[GanJi].property:
                Chu = zeiname[0]
                return SanChuanindex(Chu)
            # 第二个贼判断
            elif classDict[zeiname[1]].property == classDict[GanJi].property and\
                    classDict[zeiname[0]].property != classDict[GanJi].property:
                Chu = zeiname[1]
                return SanChuanindex(Chu)
            # 涉害法
            elif classDict[zeiname[0]].property == classDict[GanJi].property and\
                    classDict[zeiname[1]].property == classDict[GanJi].property:
                shenls = [zeiname[0], zeiname[1]]
                return SheHuiBenJia(shenls, 0)

            elif classDict[zeiname[0]].property != classDict[GanJi].property and\
                    classDict[zeiname[1]].property != classDict[GanJi].property:
                shenls = [zeiname[0], zeiname[1]]
                return SheHuiBenJia(shenls, 0)

        if true_count == 3:
            zeiname = []
            for true_condition_name in true_conditions:
                if true_condition_name == '一课':
                    zei = SiKe[0][3]
                    zeiname.append(zei)
                elif true_condition_name == '二课':
                    zei = SiKe[0][2]
                    zeiname.append(zei)
                elif true_condition_name == '三课':
                    zei = SiKe[0][1]
                    zeiname.append(zei)
                elif true_condition_name == '四课':
                    zei = SiKe[0][0]
                    zeiname.append(zei)
            samecondition = [classDict[name].property == classDict[GanJi].property for name in zeiname]
            sameshen = zip(samecondition, zeiname)
            if samecondition.count(True) == 0:
                SheHuiShangShen = []
                for bol, name in sameshen:
                    if not bol:
                        SheHuiShangShen.append(name)
                return SheHuiBenJia(SheHuiShangShen, 0)
            if samecondition.count(True) == 1:
                for bol, name in sameshen:
                    if bol:
                        Chu = name
                        return SanChuanindex(Chu)
            if samecondition.count(True) == 2:
                SheHuiShangShen = []
                for bol, name in sameshen:
                    if bol:
                        SheHuiShangShen.append(name)
                return SheHuiBenJia(SheHuiShangShen, 0)
            if samecondition.count(True) == 3:
                SheHuiShangShen = []
                for bol, name in sameshen:
                    if bol:
                        SheHuiShangShen.append(name)
                return SheHuiBenJia(SheHuiShangShen, 0)
        if true_count == 4:
            zeiname = [SiKe[0][3 - i] for i in range(4)]
            samecondition = [classDict[name].property == classDict[GanJi].property for name in zeiname]
            sameshen = zip(samecondition, zeiname)
            if samecondition.count(True) == 0:
                SheHuiShangShen = []
                for bol, name in sameshen:
                    if not bol:
                        SheHuiShangShen.append(name)
                return SheHuiBenJia(SheHuiShangShen, 0)
            if samecondition.count(True) == 1:
                for bol, name in sameshen:
                    if bol:
                        Chu = name
                        return SanChuanindex(Chu)
            if samecondition.count(True) == 2:
                SheHuiShangShen = []
                for bol, name in sameshen:
                    if bol:
                        SheHuiShangShen.append(name)
                return SheHuiBenJia(SheHuiShangShen, 0)
            if samecondition.count(True) == 3:
                SheHuiShangShen = []
                for bol, name in sameshen:
                    if bol:
                        SheHuiShangShen.append(name)
                return SheHuiBenJia(SheHuiShangShen, 0)
            if samecondition.count(True) == 4:
                SheHuiShangShen = []
                for bol, name in sameshen:
                    if bol:
                        SheHuiShangShen.append(name)
                return SheHuiBenJia(SheHuiShangShen, 0)

    # 只有克的情况
    if any(Kecondition) and not any(conditions):
        if true_kecount == 1:
            for name in sikenames:
                if true_kecondition[0] == name:
                    if name == '一课':
                        Chu = SiKe[0][3]
                    elif name == '二课':
                        Chu = SiKe[0][2]
                    elif name == '三课':
                        Chu = SiKe[0][1]
                    elif name == '四课':
                        Chu = SiKe[0][0]
            return SanChuanindex(Chu)
        if true_kecount == 2:
            kename = []
            for true_condition_name in true_kecondition:
                if true_condition_name == '一课':
                    ke = SiKe[0][3]
                    kename.append(ke)
                elif true_condition_name == '二课':
                    ke = SiKe[0][2]
                    kename.append(ke)
                elif true_condition_name == '三课':
                    ke = SiKe[0][1]
                    kename.append(ke)
                elif true_condition_name == '四课':
                    ke = SiKe[0][0]
                    kename.append(ke)
                # 第一个克判断
            if classDict[kename[0]].property == classDict[GanJi].property and \
                    classDict[kename[1]].property != classDict[GanJi].property:
                Chu = kename[0]
                return SanChuanindex(Chu)
                # 第二个克判断
            elif classDict[kename[1]].property == classDict[GanJi].property and \
                    classDict[kename[0]].property != classDict[GanJi].property:

                Chu = kename[1]
                return SanChuanindex(Chu)
                # 涉害法
            elif classDict[kename[0]].property == classDict[GanJi].property and \
                    classDict[kename[1]].property == classDict[GanJi].property:

                shenls = [kename[0], kename[1]]
                return SheHuiBenJia(shenls, 1)

            elif classDict[kename[0]].property != classDict[GanJi].property and \
                    classDict[kename[1]].property != classDict[GanJi].property:
                shenls = [kename[0], kename[1]]
                return SheHuiBenJia(shenls, 0)
        if true_kecount == 3:
            kename = []
            for true_condition_name in true_kecondition:
                if true_condition_name == '一课':
                    zei = SiKe[0][3]
                    kename.append(zei)
                elif true_condition_name == '二课':
                    zei = SiKe[0][2]
                    kename.append(zei)
                elif true_condition_name == '三课':
                    zei = SiKe[0][1]
                    kename.append(zei)
                elif true_condition_name == '四课':
                    zei = SiKe[0][0]
                    kename.append(zei)
            samecondition = [classDict[name].property == classDict[GanJi].property for name in kename]
            sameshen = zip(samecondition, kename)
            if samecondition.count(True) == 0:
                SheHuiShangShen = []
                for bol, name in sameshen:
                    if not bol:
                        SheHuiShangShen.append(name)
                return SheHuiBenJia(SheHuiShangShen, 0)
            if samecondition.count(True) == 1:
                for bol, name in sameshen:
                    if bol:
                        Chu = name
                        return SanChuanindex(Chu)
            if samecondition.count(True) == 2:
                SheHuiShangShen = []
                for bol, name in sameshen:
                    if bol:
                        SheHuiShangShen.append(name)
                return SheHuiBenJia(SheHuiShangShen, 0)
            if samecondition.count(True) == 3:
                SheHuiShangShen = []
                for bol, name in sameshen:
                    if bol:
                        SheHuiShangShen.append(name)
                return SheHuiBenJia(SheHuiShangShen, 0)
        if true_kecount == 4:
            kename = [SiKe[0][3 - i] for i in range(4)]
            samecondition = [classDict[name].property == classDict[GanJi].property for name in kename]
            sameshen = zip(samecondition, kename)
            if samecondition.count(True) == 0:
                SheHuiShangShen = []
                for bol, name in sameshen:
                    if not bol:
                        SheHuiShangShen.append(name)
                return SheHuiBenJia(SheHuiShangShen, 0)
            if samecondition.count(True) == 1:
                for bol, name in sameshen:
                    if bol:
                        Chu = name
                        return SanChuanindex(Chu)
            if samecondition.count(True) == 2:
                SheHuiShangShen = []
                for bol, name in sameshen:
                    if bol:
                        SheHuiShangShen.append(name)
                return SheHuiBenJia(SheHuiShangShen, 0)
            if samecondition.count(True) == 3:
                SheHuiShangShen = []
                for bol, name in sameshen:
                    if bol:
                        SheHuiShangShen.append(name)
                return SheHuiBenJia(SheHuiShangShen, 0)
            if samecondition.count(True) == 4:
                SheHuiShangShen = []
                for bol, name in sameshen:
                    if bol:
                        SheHuiShangShen.append(name)
                return SheHuiBenJia(SheHuiShangShen, 0)
    # 克和贼同时出现
    if any(conditions) and any(Kecondition):

        if true_count == 1:
            for name in sikenames:
                if true_conditions[0] == name:
                    if name == '一课':
                        Chu = SiKe[0][3]
                    elif name == '二课':
                        Chu = SiKe[0][2]
                    elif name == '三课':
                        Chu = SiKe[0][1]
                    elif name == '四课':
                        Chu = SiKe[0][0]
            return SanChuanindex(Chu)
        # 贼的个数为大于等于2时，使用比用法
        if true_count == 2:
            # zeiname 为四课中的天盘
            zeiname = []
            for true_condition_name in true_conditions:
                if true_condition_name == '一课':
                    zei = SiKe[0][3]
                    zeiname.append(zei)
                elif true_condition_name == '二课':
                    zei = SiKe[0][2]
                    zeiname.append(zei)
                elif true_condition_name == '三课':
                    zei = SiKe[0][1]
                    zeiname.append(zei)
                elif true_condition_name == '四课':
                    zei = SiKe[0][0]
                    zeiname.append(zei)
            # 第一个贼判断
            if classDict[zeiname[0]].property == classDict[GanJi].property and \
                    classDict[zeiname[1]].property != classDict[GanJi].property:
                Chu = zeiname[0]
                return SanChuanindex(Chu)
            # 第二个贼判断
            elif classDict[zeiname[1]].property == classDict[GanJi].property and \
                    classDict[zeiname[0]].property != classDict[GanJi].property:
                Chu = zeiname[1]
                return SanChuanindex(Chu)
            # 涉害法
            elif classDict[zeiname[0]].property == classDict[GanJi].property and \
                    classDict[zeiname[1]].property == classDict[GanJi].property:
                shenls = [zeiname[0], zeiname[1]]
                return SheHuiBenJia(shenls, 0)

            elif classDict[zeiname[0]].property != classDict[GanJi].property and \
                    classDict[zeiname[1]].property != classDict[GanJi].property:
                shenls = [zeiname[0], zeiname[1]]
                return SheHuiBenJia(shenls, 0)

        if true_count == 3:
            zeiname = []
            for true_condition_name in true_conditions:
                if true_condition_name == '一课':
                    zei = SiKe[0][3]
                    zeiname.append(zei)
                elif true_condition_name == '二课':
                    zei = SiKe[0][2]
                    zeiname.append(zei)
                elif true_condition_name == '三课':
                    zei = SiKe[0][1]
                    zeiname.append(zei)
                elif true_condition_name == '四课':
                    zei = SiKe[0][0]
                    zeiname.append(zei)
            samecondition = [classDict[name].property == classDict[GanJi].property for name in zeiname]
            sameshen = zip(samecondition, zeiname)
            if samecondition.count(True) == 0:
                SheHuiShangShen = []
                for bol, name in sameshen:
                    if not bol:
                        SheHuiShangShen.append(name)
                return SheHuiBenJia(SheHuiShangShen, 0)
            if samecondition.count(True) == 1:
                for bol, name in sameshen:
                    if bol:
                        Chu = name
                        return SanChuanindex(Chu)
            if samecondition.count(True) == 2:
                SheHuiShangShen = []
                for bol, name in sameshen:
                    if bol:
                        SheHuiShangShen.append(name)
                return SheHuiBenJia(SheHuiShangShen, 0)
            if samecondition.count(True) == 3:
                SheHuiShangShen = []
                for bol, name in sameshen:
                    if bol:
                        SheHuiShangShen.append(name)
                return SheHuiBenJia(SheHuiShangShen, 0)
        if true_count == 4:
            zeiname = [SiKe[0][3 - i] for i in range(4)]
            samecondition = [classDict[name].property == classDict[GanJi].property for name in zeiname]
            sameshen = zip(samecondition, zeiname)
            if samecondition.count(True) == 0:
                SheHuiShangShen = []
                for bol, name in sameshen:
                    if not bol:
                        SheHuiShangShen.append(name)
                return SheHuiBenJia(SheHuiShangShen, 0)
            if samecondition.count(True) == 1:
                for bol, name in sameshen:
                    if bol:
                        Chu = name
                        return SanChuanindex(Chu)
            if samecondition.count(True) == 2:
                SheHuiShangShen = []
                for bol, name in sameshen:
                    if bol:
                        SheHuiShangShen.append(name)
                return SheHuiBenJia(SheHuiShangShen, 0)
            if samecondition.count(True) == 3:
                SheHuiShangShen = []
                for bol, name in sameshen:
                    if bol:
                        SheHuiShangShen.append(name)
                return SheHuiBenJia(SheHuiShangShen, 0)
            if samecondition.count(True) == 4:
                SheHuiShangShen = []
                for bol, name in sameshen:
                    if bol:
                        SheHuiShangShen.append(name)
                return SheHuiBenJia(SheHuiShangShen, 0)
def JiuZongMen():
    try:
        return ZeiKe()
    except Exception as e:
        logger.info(f"出错：{e}")


#
for day in SIXTYJIAZI[::]:
    for solar in JIEQI.keys():
        TianPan = QiKe_TianPan(solar, day)
        print(TianPan)
        print(QiSiKe(day, TianPan)[0])
        print(QiSiKe(day, TianPan)[1])
        print(JiuZongMen())

# 打印出四课
# day = "甲子"
# hour = "更子"
# for solar in JIEQI.keys():
#     TianPan = QiKe_TianPan(solar, hour)  # 天盘月将加时
#     print(TianPan)
#     print(QiSiKe(day, TianPan)[0])  # 四课要天干支
#     print(QiSiKe(day, TianPan)[1])
#     print(JiuZongMen())
# 打印三传

# day = "甲子"
# hour = "更子"
#
# TianPan = QiKe_TianPan("惊蛰", hour)  # 天盘月将加时
# print(TianPan)
# print(QiSiKe(day, TianPan)[0])  # 四课要天干支
# print(QiSiKe(day, TianPan)[1])
# print(JiuZongMen())
# 比用法
# 涉害法
# 蒿失法
# 昴星法
# 别责法
# 八专法
# 伏吟法
# 反吟法