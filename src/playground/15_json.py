import json

data = {"a": 1, "b": ["x", "y"]}

s = json.dumps(data, ensure_ascii=False, indent=2)  # 转换为 JSON 字符串
print(f"JSON 字符串:\n{s}")

obj = json.loads(s)  # 从 JSON 字符串解析回 Python 对象
