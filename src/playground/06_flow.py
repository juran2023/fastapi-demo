# 流程控制示例

# ========== if/elif/else ==========
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"分数: {score}, 等级: {grade}")


# ========== for + range ==========
print("\n--- for + range ---")

# range(5) -> 0, 1, 2, 3, 4
for i in range(5):
    print(f"i = {i}")

# range(start, end) -> 2, 3, 4
print("\nrange(2, 5):")
for i in range(2, 5):
    print(f"i = {i}")

# range(start, end, step) -> 0, 2, 4, 6, 8
print("\nrange(0, 10, 2):")
for i in range(0, 10, 2):
    print(f"i = {i}")


# ========== enumerate ==========
print("\n--- enumerate ---")

fruits = ["apple", "banana", "cherry"]

# 不用 enumerate
print("不用 enumerate:")
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# 用 enumerate（推荐）
print("\n用 enumerate:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# 指定起始索引
print("\n从 1 开始:")
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")


# ========== while ==========
print("\n--- while ---")

count = 0
while count < 5:
    print(f"count = {count}")
    count += 1

# while + break
print("\nwhile + break:")
n = 0
while True:
    if n >= 3:
        break
    print(f"n = {n}")
    n += 1

# while + continue
print("\nwhile + continue (跳过偶数):")
i = 0
while i < 6:
    i += 1
    if i % 2 == 0:
        continue
    print(f"i = {i}")


def http_status_code(code: int) -> str:
    match code:
        case 200:
            return "OK"
        case 404:
            return "NOT FOUND"
        case _:
            return "Unknown"


print(http_status_code(787))
print(http_status_code(404))

print("\nFruits:")
for d, fruit in enumerate(fruits):
    print(d, fruit)
