nums = [1, 2, 3, 4]
squares = [n * n for n in nums if n % 2 == 0]
d = {n: n * n for n in nums}
g = (n * n for n in nums)
print(squares, d, next(g))
