def first_set_bit_in_integer(number: int):
    if not number:
        return 0
    count = 1
    while number:
        if (number & 1) == 1:
            break
        count += 1
        number >>= 1
    return count


if __name__ == '__main__':
    print(f"First set bit is: {first_set_bit_in_integer(12)}")
