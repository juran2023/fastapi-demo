# 函数示例


# ========== 基本函数 ==========
def greet(name: str) -> str:
    """
    打招呼函数

    Args:
        name: 用户名

    Returns:
        问候语字符串
    """
    return f"Hello, {name}!"


print(greet("Alice"))


# ========== 默认参数 ==========
def greet_with_title(name: str, title: str = "Mr.") -> str:
    """带称谓的问候"""
    return f"Hello, {title} {name}!"


print(greet_with_title("Smith"))  # 使用默认值
print(greet_with_title("Smith", "Dr."))  # 覆盖默认值


# ========== 多返回值 (tuple) ==========
def get_min_max(numbers: list[int]) -> tuple[int, int]:
    """
    获取列表的最小值和最大值

    Args:
        numbers: 整数列表

    Returns:
        (最小值, 最大值) 的元组
    """
    return min(numbers), max(numbers)


data = [3, 1, 4, 1, 5, 9, 2, 6]
min_val, max_val = get_min_max(data)  # 解包
print(f"最小值: {min_val}, 最大值: {max_val}")

# 也可以不解包
result = get_min_max(data)
print(f"结果元组: {result}")
print(f"最小值: {result[0]}, 最大值: {result[1]}")


# ========== 返回多个值的其他例子 ==========
def divide(a: int, b: int) -> tuple[int, int]:
    """
    整数除法，返回商和余数

    Args:
        a: 被除数
        b: 除数

    Returns:
        (商, 余数)
    """
    quotient = a // b
    remainder = a % b
    return quotient, remainder


q, r = divide(17, 5)
print(f"17 ÷ 5 = {q} 余 {r}")


# ========== *args 可变参数 ==========
def sum_all(*args: int) -> int:
    """
    求所有参数的和

    Args:
        *args: 任意数量的整数

    Returns:
        所有参数的和
    """
    return sum(args)


print(f"sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")


# ========== **kwargs 关键字参数 ==========
def build_profile(name: str, **kwargs) -> dict:
    """
    构建用户资料

    Args:
        name: 用户名
        **kwargs: 其他任意属性

    Returns:
        用户资料字典
    """
    profile = {"name": name}
    profile.update(kwargs)
    return profile


user = build_profile("Alice", age=30, city="Beijing", job="Engineer")
print(f"用户资料: {user}")


# ========== ⚠️ 坑：不要用可变对象做默认参数 ==========
print("\n--- 可变默认参数的坑 ---")


# ❌ 错误写法：用 list 做默认参数
def add_item_bad(item, items=[]):
    """这是一个有 bug 的函数！"""
    items.append(item)
    return items


# 看起来应该每次返回只有一个元素的列表？
print(add_item_bad("a"))  # ['a']       - 看起来正常
print(add_item_bad("b"))  # ['a', 'b']  - ❌ 出问题了！
print(add_item_bad("c"))  # ['a', 'b', 'c'] - ❌ 越来越多！

# 原因：默认参数 [] 只在函数定义时创建一次，之后所有调用共享同一个列表！


# ✅ 正确写法：用 None 做默认值
def add_item_good(item, items=None):
    """正确的写法"""
    if items is None:
        items = []
    items.append(item)
    return items


print("\n正确写法:")
print(add_item_good("a"))  # ['a']
print(add_item_good("b"))  # ['b'] ✅ 每次都是新列表
print(add_item_good("c"))  # ['c'] ✅


# 同样的坑也适用于 dict
# ❌ def func(data={}): ...
# ✅ def func(data=None): data = data or {}
