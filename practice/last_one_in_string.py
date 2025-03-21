
def last_one_in_string(s: str):
    index = len(s) - 1
    for i in s[-1::-1]:
        if i == "1":
            return index
        index -= 1
    return -1


if __name__ == '__main__':
    print("Last index: ", last_one_in_string("001001000"))
