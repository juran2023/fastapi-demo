import httpx

r = httpx.get("https://httpbin.org/get", timeout=10)
print(f"状态码: {r.status_code}")
print(f"响应内容: {r.url}")
