from typing import List



def min_cost_of_journey_recursive_util(red_line: List[int], blue_line: List[int], switch: int, num):
    if num == 0:
        return min(0, switch)

    else:
        red_line_cost = min(
            red_line[num] + min_cost_of_journey_recursive_util(red_line, blue_line, switch, num - 1),
            8
        )

def min_cost_of_journey_recursive(red_line: List[int], blue_line: List[int], switch: int) -> int:
    pass

def min_cost_of_journey(red_line: List[int], blue_line: List[int], switch: int) -> int:
    dr = [0] * (len(red_line) + 1)
    db = [0] * (len(blue_line) + 1)

    db[0] = switch

    for i in range(1, len(red_line) + 1):
        dr[i] = min(
            (dr[i - 1] + red_line[i - 1]),
            (db[i - 1] + blue_line[i - 1] + switch)
        )
        db[i] = min(
            (db[i - 1] + blue_line[i - 1]),
            (dr[i - 1] + red_line[i - 1] + switch)
        )
    cost = min(dr[-1], db[-1])
    print(f"RED DP: {dr}")
    print(f"BLUE DP: {db}")
    return cost


def space_optimized_min_cost_of_journey(red_line: List[int], blue_line: List[int], switch: int) -> int:
    red_cost_prev = 0
    blue_cost_prev = switch
    red_cost, blue_cost = 0, 0
    for i in range(1, len(red_line) + 1):
        red_cost = min(
            (red_cost_prev + red_line[i - 1]),
            (blue_cost_prev + blue_line[i - 1] + switch)
        )
        blue_cost = min(
            (blue_cost_prev + blue_line[i - 1]),
            (red_cost_prev + red_line[i - 1] + switch)
        )
        blue_cost_prev = blue_cost
        red_cost_prev = red_cost
    cost = min(red_cost, blue_cost)
    return cost


if __name__ == '__main__':
    print(min_cost_of_journey(red_line=[4, 2, 5, 6], blue_line=[2, 3, 3, 4], switch=2))
    print(space_optimized_min_cost_of_journey(red_line=[4, 2, 5, 6], blue_line=[2, 3, 3, 4], switch=2))