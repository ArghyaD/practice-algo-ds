from typing import List, Optional


class RodCuttingProblem:
    def recursive_solution(self, prices: List[int], n) -> int:
        if n == 0:
            return 0
        max_val = float("-inf")
        for i in range(1, n + 1):
            max_val = max(max_val, prices[i - 1] + self.recursive_solution(prices, n-i))
        return max_val

    def memoized_recursive_solution(self, prices: List[int], n, memo: Optional[List[int]]=None) -> Optional[int]:
        if not memo:
            memo = [None] * (len(prices) + 1)

        if n == 0:
            return 0
        if memo[n]:
            return memo[n]

        max_value = float("-inf")
        for i in range(1, n + 1):
            max_value = max(max_value, prices[i - 1] + self.memoized_recursive_solution(prices, n - i, memo))
        memo[n] = max_value
        return memo[n]


    def tabular_iterative_solution(self, prices):
        n = len(prices)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            max_val = float("-inf")
            for j in range(1, i + 1):
                max_val = max(max_val, prices[j - 1] + dp[i - j])
            dp[i] = max_val
        return dp[n]


if __name__ == '__main__':
    obj = RodCuttingProblem()
    print(obj.recursive_solution([1, 5, 8, 9], 4))
    print(obj.memoized_recursive_solution([1, 5, 8, 9], 4))
    print(obj.tabular_iterative_solution([1, 5, 8, 9]))
