# Typing Rules — 类型规范

本项目启用 `mypy --strict` 级别检查（`disallow_untyped_defs = true`），  
以下 5 条规则是所有 `src/` 代码的硬性约定。

---

## 1. 所有新函数必须写类型注解

函数的**参数**和**返回值**都必须标注类型，不允许出现 untyped def。

```python
# ✅ Good
def get_user(user_id: int) -> User:
    ...

# ❌ Bad
def get_user(user_id):
    ...
```

## 2. 不允许 Any 泄露

禁止在函数签名中使用 `Any`。如果确实需要泛型，请使用 `TypeVar` 或 `Generic`。  
`mypy` 配置 `warn_return_any = true` 会捕获隐式 Any 返回。

```python
# ❌ Bad
def parse(data: Any) -> Any:
    ...

# ✅ Good
from typing import TypeVar
T = TypeVar("T")
def parse(data: str, model: type[T]) -> T:
    ...
```

## 3. 优先用 dataclass / Pydantic 替代裸 dict

结构化数据**必须**用 `dataclass` 或 `pydantic.BaseModel`，  
不要传递 `dict[str, Any]` 这样的无结构类型。

```python
# ❌ Bad
def create_order(data: dict[str, Any]) -> dict[str, Any]:
    ...

# ✅ Good
class OrderCreate(BaseModel):
    product_id: int
    quantity: int

def create_order(data: OrderCreate) -> Order:
    ...
```

## 4. 可选值使用 `X | None` 而非 `Optional[X]`

统一使用 Python 3.10+ 的 `X | None` 语法，保持风格一致。

```python
# ✅ Good
def find_user(email: str) -> User | None:
    ...

# ❌ Avoid
from typing import Optional
def find_user(email: str) -> Optional[User]:
    ...
```

## 5. 容器类型必须标注元素类型

`list`、`dict`、`set`、`tuple` 等容器必须标注内部元素类型，  
不允许使用裸 `list` 或 `dict`。

```python
# ✅ Good
def get_ids() -> list[int]:
    ...

# ❌ Bad
def get_ids() -> list:
    ...
```
