def prime(n):
    lst = []
    for j in range(2, n + 1):
        flag = True
        i = 2
        while i <= j**(1/2):
            if j % i == 0:
                flag = False
                break
            i += 1

        if flag:
            lst.append(j)
    return lst


if __name__ == '__main__':
    print(prime(100))
