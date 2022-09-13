data = [x for x in range(10)]

for i in range(len(data) - 1, -1, -1):
    print(i)

print('-' * 10)

for i in reversed(data):
    print(i)
