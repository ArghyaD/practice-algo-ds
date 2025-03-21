from typing import List


class PatternSearchAlgos:
    def naive_approach(self, text: str, pattern: str):
        result = []
        n: int = len(text)
        m: int = len(pattern)
        for i in range(n-m+1):
            j: int = 0
            while j < m and text[i + j] == pattern[j]:
                j += 1

            if j == m:
                result.append(i)
        return result

    def _compute_lps(self, pattern, lps) -> None:
        i: int = 0
        j: int = 1
        n: int = len(pattern)
        while j < n:
            if pattern[i] == pattern[j]:
                i += 1
                lps[j] = i
                j += 1
            else:
                if i == 0:
                    lps[j] = 0
                    j += 1
                else:
                    i = lps[i - 1]


    def kmp_algorithm(self, text: str, pattern: str):
        m = len(pattern)
        n = len(text)
        lps = [0] * m
        result = []
        self._compute_lps(pattern, lps)
        j = 0
        i = 0
        while i < n:
            if pattern[j] == text[i]:
                i += 1
                j += 1

                if j == m:
                    result.append(i - j)
                    j = lps[j - 1]
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]
        return result


if __name__ == '__main__':
    obj = PatternSearchAlgos()
    print(obj.naive_approach(
        text="AAAAAAAAAAAAAAAAAB",
        pattern="AAAAB"
    ))
    print(obj.kmp_algorithm(
        text="AAAAAAAAAAAAAAAAAB",
        pattern="AAAAB"
    ))

    print(obj.naive_approach(
        text="aabaacaadaabaaba",
        pattern="aaba"
    ))
    print(obj.naive_approach(
        text="aabaacaadaabaaba",
        pattern="aaba"
    ))
