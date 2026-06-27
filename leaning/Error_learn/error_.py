from TestError import TestError


try:
    a = 1 + 1

except:
    pass
else:   # 没有出现错误则执行
    pass
finally:
    print(2)
    raise TestError()  # 主动抛出错误

print(2)
# NameError, ValueError, ZeroDivisionError

# 自定义错误
raise TestError("testerror")