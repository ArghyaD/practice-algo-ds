# Copied from Geeks For Geeks

N = 4


def display(arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=" ")
        print()


# Function to rotate the matrix 90 degree clockwise
def rotate90Clockwise(arr):
    global N

    # Transpose of matrix
    for i in range(N):
        for j in range(i + 1, N):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    # display(arr)

    # Reverse individual rows
    for i in range(N):
        low = 0
        high = N - 1
        while (low < high):
            arr[i][low], arr[i][high] = arr[i][high], arr[i][low]
            low = low + 1
            high = high - 1


if __name__ == '__main__':
    # Driver code
    arr = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]
    rotate90Clockwise(arr)
    display(arr)