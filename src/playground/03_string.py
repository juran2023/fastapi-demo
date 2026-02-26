import re

name = "Alice"
age = 20
print(f"{name} is {age}")
print(f"{name=}, {age=}")

s = " hello \n"
print(s.strip())
print("a,b,c".split(","))
print("".join(["a", "b", "c"]))


def to_slug(s) -> str:
    try:
        newS = re.sub(r"(?<=\w)\s+(?=\w)", "-", s.lower())
        # newS = re.sub("\s+", "-", s.lower())
        return re.sub(r"[^\w-]", "", newS)

    except TypeError:
        return None
    finally:
        print(f"raw s = {s}")


print(to_slug("Hello                          World !"))
