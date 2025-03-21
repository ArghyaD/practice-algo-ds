from typing import List

class Solution:
    def car_fleet(self, target: int, position: List[int], speed: List[int]) -> int:
        merged_list = sorted([(p, s) for p, s in zip(position, speed)])
        top = None
        result = 0
        for p, s in merged_list[::-1]:
            time = (target-p)/s
            if (not top) or (isinstance(top, float) and top < time):
                top = time
                result += 1
        return result


if __name__ == '__main__':
    print(Solution().car_fleet(target=12, position=[10,8,0,5,3], speed=[2,4,1,1,3]))