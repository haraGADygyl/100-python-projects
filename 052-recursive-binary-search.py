def recursive_binary_search(target, sequence, first, last):
    if first > last:
        return False

    mid = (first + last) // 2

    if sequence[mid] == target:
        return True
    elif target < sequence[mid]:
        return recursive_binary_search(target, sequence, first, mid-1)
    else:
        return recursive_binary_search(target, sequence, mid + 1, last)


print(recursive_binary_search(4, [1, 2, 3, 4, 5, 6, 7], 1, 7))
