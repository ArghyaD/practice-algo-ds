from typing import List


def reverse_stack_recursive(stack: List[int]):
    if stack:
        temp = stack.pop()
        reverse_stack_recursive(stack)
        reverse_stack_util(stack, temp)


def reverse_stack_util(stack: List[int], item: int):
    if not stack:
        stack.append(item)
    else:
        temp = stack.pop()
        reverse_stack_util(stack, item)
        stack.append(temp)


def print_stack(stack):
    for i in stack[::-1]:
        print(i)


if __name__ == '__main__':
    some_stack: List[int] = [3, 2, 1, 4]
    print("Initial Stack")
    print_stack(stack=some_stack)
    reverse_stack_recursive(some_stack)
    print("Reverse Stack")
    print_stack(stack=some_stack)

    '''
        For the iterative approach, we will implement the stack using Linked List and use Linked List Reversal logic
    '''