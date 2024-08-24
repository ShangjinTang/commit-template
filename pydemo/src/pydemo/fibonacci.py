from typing import Iterator


def fibonacci(n: int) -> Iterator[int]:
    current, next_value = 0, 1
    for _ in range(n):
        yield current
        current, next_value = next_value, current + next_value
