class User:
    def __init__(self, name: str, age: int = 0):
        self._name = name
        self._age = age

    def name(self) -> str:
        return self._name

    def greet(self):
        print(f"Hello! {self._name}")

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        """从字典创建 User 对象"""
        return cls(name=data["name"], age=data.get("age", 0))


a = User("Alex")
print(a.name())
a.greet()

# 测试 from_dict
user_data = {"name": "Bob", "age": 25}
b = User.from_dict(user_data)
print(f"从字典创建: {b.name()}, 年龄: {b._age}")
