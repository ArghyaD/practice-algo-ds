
def edit_distance(string1: str, string2: str):
    n1 = len(string1)
    n2 = len(string2)
    dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]


    for i in range(n1):
        dp[0][i] = i
    for i in range(n2):
        dp[i][0] = i

    for i in range(1, n2 + 1):
        for j in range(1, n1 + 1):
            if string2[i - 1] == string1[j - 1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
    return dp[n2][n1]


if __name__ == '__main__':
    print(edit_distance("pad", "grade"))