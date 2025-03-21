
def sample_decorator(func):
    def wrapper(*args, **kwargs):
        import time
        time_b = time.time_ns()
        result = func(*args, **kwargs)
        time_c = time.time_ns()
        print(f"Time taken: {time_c - time_b}")
        return result
    return wrapper


def _lcs_naive_util(text1: str, text2: str, m: int, n: int):
    if m == 0 or n == 0:
        return 0

    if text1[m] == text2[n]:
        return 1 + _lcs_naive_util(text1, text2, m-1, n-1)
    else:
        return max(
            _lcs_naive_util(text1, text2, m-1, n),
            _lcs_naive_util(text1, text2, m, n-1)
        )

@sample_decorator
def lcs_naive(text1: str, text2: str):
    m = len(text1)
    n = len(text2)
    return _lcs_naive_util(text1, text2, m - 1, n - 1)


def _lcs_memoized_util(text1: str, text2: str, m: int, n: int, memo):
    if m == 0 or n == 0:
        return 0

    if memo[m][n] != -1:
        return memo[m][n]

    if text1[m] == text2[n]:
        memo[m][n] = 1 + _lcs_memoized_util(text1, text2, m-1, n-1, memo)
    else:
        memo[m][n] = max(
            _lcs_memoized_util(text1, text2, m-1, n, memo),
            _lcs_memoized_util(text1, text2, m, n-1, memo)
        )
    return memo[m][n]

@sample_decorator
def lcs_memoized(text1: str, text2: str):
    m = len(text1)
    n = len(text2)
    memo = [[-1] * m for _ in range(n)]
    return _lcs_memoized_util(text1, text2, m - 1, n - 1, memo)


@sample_decorator
def lcs_optimized(text1: str, text2: str):
    m = len(text1)
    n = len(text2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if text1[i] == text2[j]:
                dp[i + 1][j + 1] = 1 + dp[i][j]
            else:
                dp[i + 1][j + 1] = max(
                    dp[i + 1][j],
                    dp[i][j + 1]
                )

    return dp[m][n]

@sample_decorator
def lcs_space_optimized(text1: str, text2: str):
    m = len(text1)
    n = len(text2)
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)
    for i in range(m):
        for j in range(n):
            if text1[i] == text2[j]:
                curr[j + 1] = 1 + prev[j]
            else:
                curr[j + 1] = max(prev[j + 1], curr[j])
        prev = curr[:]
    return curr[j+1]


if __name__ == '__main__':
    print(lcs_naive("ABCFGHEWR", "QWDFRHEWR"))
    print(lcs_memoized("ABCFGHEWR", "QWDFRHEWR"))
    print(lcs_optimized("ABCFGHEWR", "QWDFRHEWR"))
    print(lcs_space_optimized("ABCFGHEWR", "QWDFRHEWR"))
