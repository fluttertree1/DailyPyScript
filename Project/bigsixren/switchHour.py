def switchtime(hour, minute):
    if 0 <= hour <= 24 and 0 <= minute <= 60:
        if 0 <= hour and (minute <= 59 and hour < 1):
            hourzhi = "子"
            return hourzhi
        if 23 <= hour and (minute <= 59 and hour < 24):
            hourzhi = "子"
            return hourzhi
        if 1 <= hour and (minute <= 59 and hour < 3):
            hourzhi = "丑"
            return hourzhi
        if 3 <= hour and (minute <= 59 and hour < 5):
            hourzhi = "寅"
            return hourzhi
        if 5 <= hour and (minute <= 59 and hour < 7):
            hourzhi = "卯"
            return hourzhi
        if 7 <= hour and (minute <= 59 and hour < 9):
            hourzhi = "辰"
            return hourzhi
        if 9 <= hour and (minute <= 59 and hour < 11):
            hourzhi = "巳"
            return hourzhi
        if 11 <= hour and (minute <= 59 and hour < 13):
            hourzhi = "午"
            return hourzhi
        if 13 <= hour and (minute <= 59 and hour < 15):
            hourzhi = "未"
            return hourzhi
        if 15 <= hour and (minute <= 59 and hour < 17):
            hourzhi = "申"
            return hourzhi
        if 17 <= hour and (minute <= 59 and hour < 19):
            hourzhi = "酉"
            return hourzhi
        if 19 <= hour and (minute <= 59 and hour < 21):
            hourzhi = "戌"
            return hourzhi
        if 21 <= hour and (minute <= 59 and hour < 23):
            hourzhi = "亥"
            return hourzhi


