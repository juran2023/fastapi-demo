"""
Python 7.2 读写文件 & 文件对象的方法 & json 保存结构化数据
对应: https://docs.python.org/zh-cn/3.14/tutorial/inputoutput.html#reading-and-writing-files
"""

import json
import os

# 确保在脚本所在目录操作临时文件
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ============================================================
# 7.2 读写文件 —— open() 与 with 语句
# ============================================================
# open(filename, mode, encoding=...)
# mode: 'r' 读(默认), 'w' 写(会截断), 'a' 追加, 'r+' 读写
#       加 'b' 表示二进制模式，如 'rb', 'wb'

# 推荐使用 with，自动关闭文件
with open(r"C:\Users\pc\Downloads\test_src.txt", "r", encoding="utf-8") as f:
    # content = f.read()

    # lines = f.readlines()
    # for line in lines:
    #     print(line.strip())
    # print([x.replace("\n", "") for x in lines if x.strip()])  # 去掉空行
    while True:
        line = f.readline()
        if not line:
            break
        print(line.strip())

print("--- 文件已关闭:", f.closed)  # True

# ============================================================
# 7.2.1 文件对象的方法
# ============================================================

# ---------- f.read() ----------
# 读取全部内容（或指定 size 个字符）
# with open("workfile.txt", "r", encoding="utf-8") as f:
#     content = f.read()
#     print("--- f.read() 读取全部内容:")
#     print(content)

with open(r"C:\Users\pc\Downloads\test_src.txt", "r", encoding="utf-8") as f:
    partial = f.read(5)  # 只读 5 个字符
    print(f"--- f.read(5): '{partial}'")
    rest = f.read()  # 读取剩余
    print(f"--- f.read() 剩余: '{rest}'", end="")
    eof = f.read()  # 到达末尾返回空字符串
    print(f"--- 到达 EOF: '{eof}'")

# # ---------- f.readline() ----------
# # 每次读取一行，保留末尾的 \n；到达 EOF 返回空字符串
# print("\n--- f.readline() 逐行读取:")
# with open("workfile.txt", "r", encoding="utf-8") as f:
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         print(f"  {line!r}")

# # ---------- 遍历文件对象（推荐方式）----------
# # 直接 for 循环迭代，内存高效
# print("\n--- for line in f（推荐）:")
with open(r"C:\Users\pc\Downloads\test_src.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(f"  {line!r}")

# # ---------- f.readlines() / list(f) ----------
# # 一次性读取所有行到列表
with open(r"C:\Users\pc\Downloads\test_src.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(f"\n--- f.readlines(): {lines}")

# # ---------- f.write() ----------
# # 写入字符串，返回写入的字符数
# with open("workfile.txt", "a", encoding="utf-8") as f:
#     num_chars = f.write("kiriko\n")
#     print(f"\n--- f.write() 写入了 {num_chars} 个字符")

# # 写入非字符串需要先转换
# with open("workfile.txt", "a", encoding="utf-8") as f:
#     value = ("答案是", 42)
#     s = str(value)
#     num = f.write(s + "\n")
#     print(f"--- 写入元组的字符串形式: {s}, 共 {num} 字符")

# # ---------- f.tell() ----------
# # 返回文件对象在文件中的当前位置（字节偏移量）
with open("workfile.txt", "rb") as f:
    print(f"\n--- f.tell() 初始位置: {f.tell()}")
    f.read(10)
    print(f"--- 读取 10 字节后位置: {f.tell()}")

# # ---------- f.seek(offset, whence) ----------
# # whence: 0=文件开头(默认), 1=当前位置, 2=文件末尾
# # 文本模式下只允许 seek(0) 或 seek(tell()的返回值)
# # 二进制模式下可以自由 seek
with open("workfile.txt", "rb") as f:
    f.seek(0, 2)  # 移到文件末尾
    size = f.tell()
    print(f"--- 文件大小: {size} 字节")

    f.seek(0)  # 回到开头
    print(f"--- seek(0) 后位置: {f.tell()}")

    f.seek(-6, 2)  # 从末尾倒退 6 字节
    tail = f.read()
    print(f"--- 末尾 6 字节: {tail!r}")

# # ============================================================
# # 7.2.2 使用 json 保存结构化数据
# # ============================================================
print("\n" + "=" * 50)
print("7.2.2 使用 json 保存结构化数据")
print("=" * 50)

# json.dumps() —— 序列化为字符串
data = [1, "simple", "list"]
json_str = json.dumps(data)
print(f"\n--- json.dumps(): {json_str}")

# json.dump() —— 序列化并写入文件
# data = {"name": "Alice", "age": 30, "hobbies": ["reading", "coding"]}
# with open("data.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, ensure_ascii=False, indent=2)
#     print("--- json.dump() 已写入 data.json")

# # json.load() —— 从文件反序列化
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
    print(f"--- json.load(): {loaded}")
    print(f"--- 类型: {type(loaded)}")

# # json.loads() —— 从字符串反序列化
json_string = '{"key": "value", "number": 42}'
parsed = json.loads(json_string)
print(f"--- json.loads(): {parsed}")

# # ============================================================
# # 清理临时文件
# # ============================================================
# os.remove("workfile.txt")
# os.remove("data.json")
# print("\n--- 临时文件已清理")
