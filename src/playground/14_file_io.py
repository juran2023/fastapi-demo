from pathlib import Path


p = Path("docs") / "sample.txt"
# p.write_text("hello\n", encoding="utf-8")
with open(p, "a", encoding="utf-8") as f:
    f.write("拉拉的瑞")

print(p.read_text(encoding="utf-8"))
