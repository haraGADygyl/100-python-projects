def sequential_search(arr, n):
    for i in arr:
        if i == n:
            return 'Found!'
    return 'Not found!'


data = list(range(30))
print(sequential_search(data, 12))
