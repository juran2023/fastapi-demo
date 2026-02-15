from pydantic import BaseModel, Field


class UserIn(BaseModel):
    email: str
    age: int = Field(ge=0, le=120)  # 年龄必须在 0 到 120 之间


user1 = UserIn(email="test@example.com", age=25)
# user = UserIn(email="test@example.com", age=122) # 会抛出 ValidationError，因为 age 超出范围
