"""
自定义错误类型
"""


class TestError(Exception):
    def __init__(self, message="Test"):
        self.message = message

    def __str__(self):
        return "%s" % self.message
