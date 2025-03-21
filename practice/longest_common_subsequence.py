from typing import List


def naive_lcs(arr1: str, arr2: str, m: int, n: int) -> int:
    if m == 0 or n == 0:
        return 0
    if arr1[m-1] == arr2[n-1]:
        return 1 + naive_lcs(arr1, arr2, m-1, n-1)
    else:
        return max(naive_lcs(arr1, arr2, m-1, n), naive_lcs(arr1, arr2, m, n-1))


def memoized_naive_lcs(arr1: str, arr2: str, m: int, n: int, buff: List[List[int]]):
    if m == 0 or n == 0:
        return 0

    if buff[m][n] != -1:
        return buff[m][n]

    if arr1[m-1] == arr2[n-1]:
        buff[m][n] = 1 + memoized_naive_lcs(arr1, arr2, m-1, n-1, buff)

    else:
        buff[m][n] = max(memoized_naive_lcs(arr1, arr2, m - 1, n, buff), memoized_naive_lcs(arr1, arr2, m, n - 1, buff))

    return buff[m][n]

if __name__ == '__main__':
    s1 = "AGGTAB"
    s2 = "GXTXAYB"
    m = len(s1)
    n = len(s2)

    print(naive_lcs(s1, s2, m, n))

    buffer = [[-1 for _ in range(n+1)] for _ in range(m+1)]
    print(memoized_naive_lcs(s1, s2, m, n, buffer))