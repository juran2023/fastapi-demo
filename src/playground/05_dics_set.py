user = {"id": 1, "name": "bob"}

print(user.get("emial", "no email"))
user["name"] = "leave"
print(user)

s = set([1, 2, 2, 3])
print(s)


def group_by(items: list, key_func) -> dict:
    """根据 key_func 返回值对列表元素进行分组"""
    result = {}
    for item in items:
        key = key_func(item)
        if key not in result:
            result[key] = []
        result[key].append(item)
    return result


# 测试
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 25},
    {"name": "David", "age": 30},
]

# 按年龄分组
print(group_by(users, lambda u: u["age"]))
# {25: [{"name": "Alice", ...}, {"name": "Charlie", ...}], 30: [...]}

# 按名字首字母分组
print(group_by(users, lambda u: u["name"][0]))
