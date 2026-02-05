x = 1
y = 1.5
ok = True
n = None

print(type(x), type(y), type(ok), type(n))
print(int("42"), float("3.14"), bool(0), bool(1))


def safe_int(s) -> int | None:
    try:
        return int(float(s))  # 先转 float 再转 int，支持 "11.1" 这样的输入
    except (ValueError, TypeError):
        return None


print(safe_int("11.1"))
print(safe_int("xi jin ping"))
