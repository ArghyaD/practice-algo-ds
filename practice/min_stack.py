from typing import List


class MinStack:
    """
        Script to create a stack with following operations:
            1. push
            2. pop
            3. get_min
        All the above-mentioned operations should have a time complexity of O(1)
    """

    def __init__(self):
        self.stack: List = []
        self.min: int = -1
        self.dummy_value: int = 999999999999

    def push(self, x):
        if x < self.min or not self.stack:
            self.min = x
        self.stack.append(x * self.dummy_value + self.min)

    def pop(self):
        if not self.stack:
            self.min = -1
            return None
        self.min = self.stack[-1] % self.dummy_value
        return self.stack.pop() // self.dummy_value

    def get_min(self):
        return self.min


if __name__ == '__main__':
    min_stack: MinStack = MinStack()
    min_stack.push(12)
    min_stack.push(9)
    min_stack.push(7)

    print("Current min: ", min_stack.get_min())

    min_stack.push(17)
    min_stack.push(3)
    min_stack.push(12)

    print("Current min: ", min_stack.get_min())

    min_stack.push(1)

    print("Current min: ", min_stack.get_min())

    print("Popped value: ", min_stack.pop())
    print("Popped value: ", min_stack.pop())

    print("Current min: ", min_stack.get_min())

    print("Popped value: ", min_stack.pop())
    print("Popped value: ", min_stack.pop())

    print("Current min: ", min_stack.get_min())

    print("Popped value: ", min_stack.pop())
    print("Popped value: ", min_stack.pop())
    print("Popped value: ", min_stack.pop())

    print("Current min: ", min_stack.get_min())

    print("Popped value: ", min_stack.pop())
