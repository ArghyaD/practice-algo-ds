
def reverse_words_of_sentence(S: str):
    buffer = S.split(".")
    start = 0
    end = len(buffer) - 1
    while start < end:
        buffer[start], buffer[end] = buffer[end], buffer[start]
        start += 1
        end -= 1
    return ".".join(buffer)


if __name__ == '__main__':
    print(reverse_words_of_sentence("i.like.this.program.very.much"))

