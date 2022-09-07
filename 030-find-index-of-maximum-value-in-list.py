import time


def find_maximum(a):
    return a.index(max(a))


start = time.time()
print(find_maximum([x for x in range(10_000_000)]))
print(time.time() - start)


def find_maximum2(a):
    max_index = 0
    current_index = 0

    while current_index < len(a):
        if a[current_index] > a[max_index]:
            max_index = current_index
        else:
            current_index += 1

    return max_index


start2 = time.time()
print(find_maximum2([x for x in range(10_000_000)]))
print(time.time() - start2)
