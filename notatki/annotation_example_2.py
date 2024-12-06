from typing import TypeVar

T = TypeVar("T", int, str, float)

def add(a: T, b: T) -> T:
    return a + b

add(1, 2)
add("a", "b")
add(2.1, 2.3)
