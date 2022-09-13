def count_negatives(arr):
    count = 0
    row_i = 0
    col_i = len(arr[0]) - 1

    while col_i >= 0 and row_i < len(arr):
        if arr[row_i][col_i] < 0:
            count += col_i + 1
            row_i += 1
        else:
            col_i -= 1

    return count


def count_negatives2(arr):
    result = 0

    for i in arr:
        for j in i:
            if j < 0:
                result += 1

    return result


print(count_negatives(
    [[-4, -3, -1, 1],
     [-2, -2, 1, 2],
     [-1, 1, 2, 3],
     [1, 2, 4, 5]]))

print(count_negatives(
    [[-1, 0],
     [0, 0]]))

print(count_negatives(
    [[-2, 0],
     [-1, 0]]))

print(count_negatives([[0]]))
