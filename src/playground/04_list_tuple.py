a = [1, 2, 3]
a.append("4")

print(a[1:4])
print(a)
t = (1, 2)
print(t)


def chunk_list(lst: list, size: int) -> list[list]:
    """把列表分成指定大小的块"""
    return [lst[i : i + size] for i in range(0, len(lst), size)]


# 测试
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(chunk_list(data, 3))  # [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
