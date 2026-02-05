def f(a, b, *args, c=1, **kwargs):
    print(a, b, args, c, kwargs)


f(1, 2, 3, 4, c=10, x=99)


def build_url(base: str, **query) -> str:
    """
    构建带查询参数的 URL

    Args:
        base: 基础 URL
        **query: 查询参数

    Returns:
        完整的 URL
    """
    if not query:
        return base
    query_string = "&".join(f"{k}={v}" for k, v in query.items())
    return f"{base}?{query_string}"


# 测试
print(build_url("https://api.example.com/users", page=1, limit=10, sort="name"))
# 输出: https://api.example.com/users?page=1&limit=10&sort=name
