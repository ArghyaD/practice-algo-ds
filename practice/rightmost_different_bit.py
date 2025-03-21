from typing import List
import math

class RightMostDifferentBit:
    def _bin_repr(self, num) -> List[int]:
        result: List[int] = []
        while num > 0:
            result.append(num % 2)
            num //= 2
        return result

    def naive_solution(self, m: int, n: int) -> int:
        m_bin_repr: List[int] = self._bin_repr(m)
        n_bin_repr: List[int] = self._bin_repr(n)
        till = min(len(m_bin_repr), len(n_bin_repr))

        for i in range(till):
            if int(m_bin_repr[i]) ^ int(n_bin_repr[i]):
                return i
        return till + 1

    def solution(self, m: int, n: int) -> int:
        o: int = m ^ n
        o_bin_repr: List[int] = self._bin_repr(o)
        for i in range(len(o_bin_repr)):
            if o_bin_repr[i]:
                return i

    def optimized_solution(self, m: int, n: int) -> int:
        """
           So, here's how this works:
           If log to the base x of a number y is z that basically indicates x ** z (x raised to the power of z)
           is equals to y.

           Now when we do x XOR y, the result of that has all the bits set (equal to 1) for bits which are
           equal/identical and unset (equal to 0) for bits which are equal.

           So, once we have that all we need is the right most set bit.

           For that we use log to the base 2 of ((x XOR y) & -(x XOR y))


        :param m:
        :param n:
        :return:
        """
        xored_value: int = m ^ n
        return int(math.log2(xored_value & -xored_value))

if __name__ == '__main__':
    obj = RightMostDifferentBit()
    print(obj.naive_solution(m=11, n=9))
    print(obj.solution(m=11, n=9))
    print(obj.optimized_solution(m=11, n=9))
    print(obj.naive_solution(m=52, n=4))
    print(obj.solution(m=52, n=4))
    print(obj.optimized_solution(m=52, n=4))
