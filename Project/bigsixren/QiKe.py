TIANGAN = "甲乙丙丁戊己庚辛壬癸"  # 0-9
DIZHI = "子丑寅卯辰巳午未申酉戌亥"  # 0-11
JIEQI = {  # 节气与月将对应表(简化版)
    '立春': '寅', '雨水': '卯', '惊蛰': '辰', '春分': '巳',
    '清明': '午', '谷雨': '未', '立夏': '申', '小满': '酉',
    '芒种': '戌', '夏至': '亥', '小暑': '子', '大暑': '丑'
}


def QiKe_TianPan(solar, HourGanZhi):  # 字符串
    index = []
    general = JIEQI[solar]

    gidx = DIZHI.index(general)
    index.append(gidx)
    hidx = DIZHI.index(HourGanZhi[1])
    index.append(hidx)
    # index[0] 月将  index[1] 时支
    if index[0] > index[1]:  # 月将位置比时支靠前
        diff = index[0] - index[1]
        TianPan = DIZHI[diff::] + DIZHI[:diff:]
        return TianPan
    if index[0] < index[1]:  # 月将位置比时支靠后
        diff = 11 - (index[1] - index[0])
        TianPan = DIZHI[diff+1::] + DIZHI[:diff+1:]
        return TianPan
    if index[0] == index[1]:
        TianPan = DIZHI
        return TianPan


def JiGong(day):
    if day[0] == "甲":
        GanJi = "寅"
        return GanJi
    if day[0] == "乙":
        GanJi = "辰"
        return GanJi
    if day[0] == "丙":
        GanJi = "巳"
        return GanJi
    if day[0] == "丁":
        GanJi = "未"
        return GanJi
    if day[0] == "戊":
        GanJi = "巳"
        return GanJi
    if day[0] == "己":
        GanJi = "未"
        return GanJi
    if day[0] == "庚":
        GanJi = "申"
        return GanJi
    if day[0] == "辛":
        GanJi = "戌"
        return GanJi
    if day[0] == "壬":
        GanJi = "亥"
        return GanJi
    if day[0] == "癸":
        GanJi = "丑"
        return GanJi


def QiSiKe(day, TianPan):
    GanJi = JiGong(day)

    GanLandIdx = DIZHI.index(GanJi)
    GanYang = TianPan[GanLandIdx]
    GanYangIdx = DIZHI.index(GanYang)
    GanYin = TianPan[GanYangIdx]

    ZhiLandIdx = DIZHI.index(day[1])
    ZhiYang = TianPan[ZhiLandIdx]
    ZhiYangIdx = DIZHI.index(ZhiYang)
    ZhiYin = TianPan[ZhiYangIdx]

    return [[ZhiYin, ZhiYang, GanYin, GanYang],
            [ZhiYang, day[1], GanYang, day[0]]]

