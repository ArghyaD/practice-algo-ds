from typing import List, Dict


def are_brackets_balanced(expr: str):
    bracket_tracker: Dict[str, str] = {
        "}": "{",
        "]": "[",
        ")": "("
    }

    bracket_buffer: List[str] = []

    for i in expr:
        if i in ["{", "[", "("]:
            bracket_buffer.append(i)
        else:
            if not bracket_buffer:
                return False
            top_element: str = bracket_buffer.pop()
            if top_element != bracket_tracker[i]:
                return False

    if bracket_buffer:
        return False
    return True


if __name__ == '__main__':
    response: bool = are_brackets_balanced("{{()()[]({})}(()}")
    messsage: str = "Balanced" if response else "Unbalanced"
    print(messsage)
