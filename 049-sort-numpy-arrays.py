

import time

import numpy as np

a = np.array([x for x in range(100_000_000, 0, -1)])

start = time.time()
print('numpy sorting: ', np.sort(a))
print(time.time() - start)


def sorting(arr):
    for i in range(len(arr)):
        swap = i + np.argmin(arr[i:])
        arr[i], arr[swap] = arr[swap], arr[i]
    return ''


start2 = time.time()
print('your sorting: ', sorting([x for x in range(10_000, 0, -1)]))
print(time.time() - start2)
