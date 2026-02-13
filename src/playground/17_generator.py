def gen(n: int):
    for i in range(n):
        yield i * i  # 生成 i 的平方


for x in gen(7):
    print(x)
