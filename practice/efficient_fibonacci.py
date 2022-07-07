
from typing import List, Optional


def memoized_fibonacci(n: int, memo: List[Optional[int]] = None) -> int:
    if not memo:
        memo = [None] * n
    if memo[n - 1] is not None:
        return memo[n - 1]
    if n in [1, 2]:
        return 1
    memo[n - 1] = memoized_fibonacci(n-1, memo) + memoized_fibonacci(n - 2, memo)
    return memo[n - 1]


def bottom_up_fibonacci(n):
    if n == 1 or n == 2:
        return 1
    memo: List[Optional[int]] = [None] * n
    memo[0] = memo[1] = 1
    for element in range(2, n):
        memo[element] = memo[element - 1] + memo[element - 2]
    return memo[n - 1]


if __name__ == "__main__":
    print(bottom_up_fibonacci(100000))
    print(memoized_fibonacci(999)) # Highest
