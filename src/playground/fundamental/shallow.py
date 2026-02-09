x = [1, 2, 3, 4, 5]

y = x[1:3]  ## [2. 3]

y[0] = 3  ## [3. 3]

print(y)

print(x)


x = [{"name": 1, "info": {"age": 1}}, {"name": 2, "info": {"age": 2}}]

y = x[:1]

y[0]["info"]["age"] = 3  # 字典用 [] 访问，不是 .

print(x)
print(y)
