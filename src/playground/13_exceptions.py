def BizError(Exception):
    pass


def must_be_positive(x: int) -> int:
    if x <= 0:
        raise BizError("x 必须是正数")
    return x


must_be_positive(10)  # 正常返回 10

must_be_positive(-5)  # 抛出 BizError: x 必须是正数
