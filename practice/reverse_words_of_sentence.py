from typing import List


def reverse_words_of_sentence(string_to_convert: str) -> str:
    buffer: List[str] = string_to_convert.split(".")
    start: int = 0
    end: int = len(buffer) - 1
    while start < end:
        buffer[start], buffer[end] = buffer[end], buffer[start]
        start += 1
        end -= 1
    return ".".join(buffer)


if __name__ == '__main__':
    print(reverse_words_of_sentence("i.like.this.program.very.much"))

